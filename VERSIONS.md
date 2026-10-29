# Versions

Resolved in `uv.lock` on 2026-10-29. "Previous" is the old `requirements.txt` (2020-2021 pins).

| Component | Version | Previous | Note |
|---|---|---|---|
| Python | 3.13 (resolved 3.13.18) | 3.8/3.9 | `requires-python >=3.13` |
| Django | 5.2.18 | 3.1.1 | 5.2 is the LTS line (6.1.x is newer but not LTS) |
| django-ckeditor | 6.7.4 | 6.0.0 | bundles CKEditor 4.22.1, unsupported with unfixed security issues; see work-done.md |
| django-crispy-forms | 2.7 | 1.11.1 | |
| crispy-bootstrap4 | 2026.2 | n/a | required by crispy-forms 2.x |
| django-embed-video | 1.4.10 | 1.4.0 | |
| Pillow | 13.0.0 | 8.1.2 | |
| WhiteNoise | 6.12.0 | 5.2.0 | |
| dj-database-url | 3.1.2 | 0.5.0 | |
| gunicorn | 26.2.0 | 20.0.4 | |
| psycopg | 3.3.6 (binary) | psycopg2 2.8.6 | |

Removed as unused (no import in code or templates): django-allauth, djangorestframework, django-filter, django-extensions, Django-Verify-Email, validate-email, requests, pyOpenSSL/cryptography/PyJWT/oauthlib stack, and dev tools black, pylint, isort, mypy-extensions. Removed as unmaintained: django-heroku.

Dev: pytest, pytest-django, ruff.
