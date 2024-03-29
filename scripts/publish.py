import argparse
import subprocess
import sys

import semver

import scripts.utils as utils

logger = utils.setup(__name__)


def _parse_version(version: str) -> str:
    short_version = ""
    is_prerelease = True

    if version == "main":
        short_version = version
    else:
        try:
            sv = semver.Version.parse(version.removeprefix("v"))
            short_version = f"v{sv.major}.{sv.minor}"
            is_prerelease = sv.prerelease is not None
        except ValueError as e:
            logger.warn(e)

    logger.info("%s (is_prerelease: %s)", short_version, is_prerelease)
    return short_version, is_prerelease


def mike(args: list[str]) -> None:
    rc = subprocess.run(
        ["mike"] + args,
        stdout=sys.stdout,
        stderr=sys.stderr,
    )
    if rc.returncode != 0:
        raise Exception(rc.stderr)

def is_initial() -> bool:
    rc = subprocess.run(
        ["git", "show-ref", "--quiet", "refs/heads/gh-pages"],
    )
    return rc.returncode != 0

def run(args=sys.argv):
    parser = argparse.ArgumentParser(
        prog="publish",
        description="script to build and publish documentation of registry-operator docs",
    )
    parser.add_argument(
        "--version",
        help="tagged version which should be built",
        default="main",
        type=str,
        required=False,
    )

    args = parser.parse_args(args=args[1:])

    version, prerelease = _parse_version(version=args.version)
    if is_initial():
        mike(["deploy", "--push", "--update-aliases", version, "latest"])
        mike(["set-default", "--push", "latest"])
    else:
        if prerelease:
            mike(["deploy", "--push", "--update-aliases", version])
        else:
            mike(["deploy", "--push", "--update-aliases", version, "latest"])
