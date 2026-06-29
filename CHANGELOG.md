# Changelog

parse-changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Security
* Harden changelog writes against fixed temporary-file symlink overwrites.
* Harden the release workflow by validating computed versions and avoiding raw GitHub expression injection in shell commands.

### Changed
* Build release distributions with the standard Python build frontend and validate package metadata before publishing.
* Move automated changelog commits and release tags after successful PyPI publishing.

### Fixed
* Fix Linux release packaging so the generated wheel keeps the intended version and uses metadata supported by the publish action.

## [1.0.8] - 2023-10-24
### Fixed
* Update and correct README

## [1.0.7] - 2023-10-24
### Added
* Add option to add a change to the changelog
### Fixed
* Fix extra newline being added at end of file

## [1.0.6] - 2023-10-23
### Changed
* Update pipeline to auto-tag and release on push to main

## [1.0.3] - 2023-07-25
### Fixed
* Fix date parsing in release title
### Changed
* Use pypi trusted publishing to publish package

## [1.0.2] - 2022-12-08
### Fixed
* Fix writing wrong filename when using -c option
* Fix adding a release that already exists

## [1.0.1] - 2022-12-08
### Changed
* Better documentation

## [1.0.0] - 2022-10-20
Initial release
