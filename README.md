# Docs

Source files of documentation for Registry Operator.

[![GitHub License](https://img.shields.io/github/license/registry-operator/docs)][license]
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)
[![GitHub issues](https://img.shields.io/github/issues/registry-operator/docs)](https://github.com/registry-operator/docs/issues)
[![GitHub release](https://img.shields.io/github/release/registry-operator/docs)](https://GitHub.com/registry-operator/docs/releases/)

Join the community to discuss ongoing operator development and usage in [#registry-operator](https://cloud-native.slack.com/archives/C06P7RC8857) channel on the CNCF Slack.

[![Slack Channel](https://img.shields.io/badge/Slack-CNCF-4A154B?logo=slack)](https://cloud-native.slack.com/archives/C06P7RC8857)

<!-- Resources -->

[license]: https://github.com/registry-operator/docs/blob/main/LICENSE

## Developing

### Setting Up Environment

Ensure you have Python and Poetry installed on your system.

```sh
poetry install
```

### Code Formatting and Linting

To ensure code consistency and quality, use the following commands:

```sh
poetry run black .
poetry run isort --profile=black .
poetry run mypy .
```

## Previewing Documentation Locally

To preview the documentation locally, run the following command:

```sh
poetry run mkdocs serve
```

## Publishing

### Automated Release with release-please

The `release-please` tool automates the release process by generating release PRs with version bumps and changelogs.

### Automated Release from main branch

Each commit to the `main` branch is automatically released to the `main` tag on the page.

## Manual Release from Main Branch

To manually release from the `main` branch, follow these steps:

```sh
poetry run publish
```
