# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and versioning follows [Semantic Versioning](https://semver.org/).

## [0.3.0] - 2026-09-28
### Added
- Environment-specific settings: `configsite/settings_dev.py` and
  `configsite/settings_prod.py`, both importing the shared base `settings.py`.
- Production settings read `SECRET_KEY` and `ALLOWED_HOSTS` from environment
  variables and fail immediately with a `KeyError` if they are missing.
- HTTPS hardening in production settings: `SECURE_SSL_REDIRECT`,
  `SESSION_COOKIE_SECURE`, `CSRF_COOKIE_SECURE`, `SECURE_HSTS_SECONDS`.
- Rebuilt distributable artifacts (`.whl` and `.tar.gz`) so they include the new
  settings files (the 0.2.0 build predated them).
- Real Django test (`core/tests.py`, `PackagingSanityTests`) verifying the `core`
  app is installed, run via `manage.py test`.
- SHA-256 checksums for both build artifacts (`dist/CHECKSUMS.sha256`), verified
  with `sha256sum -c`.

### Fixed
- `core/tests.py` originally imported `TestCase` while the test class used
  `SimpleTestCase`, causing `NameError: name 'SimpleTestCase' is not defined`.
  Corrected the import to match the class actually used.

## [0.2.0] - 2026-09-26
### Added
- `core` Django app, registered in `INSTALLED_APPS`.

## [0.1.0] - 2026-09-26
### Added
- Initial Django project (`configsite`) scaffolded with `django-admin startproject`.
- `pyproject.toml` dependency manifest with version ranges for Django, asgiref,
  and sqlparse, plus `[build-system]` configuration (setuptools backend).
- `requirements.lock.txt` generated with `pip-compile`, pinning exact versions
  of all dependencies including transitive ones.
- `[tool.setuptools.packages.find]` added to restrict package discovery to
  `core*` and `configsite*` after a build failure caused by setuptools
  mistaking the `screenshots/` folder for a Python package.
