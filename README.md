# Web News Nepal

## Overview  

**webNewsNepal** is a Django news publishing site with category pages, user accounts, media uploads, and an admin interface.

---

## Features

- Home page with paginated posts (6 per page, newest first) and post detail pages.
- 13 category pages: national, covid, politics, international, sports, entertainment, lifestyle, blog, literature, health, education, business, tech.
- Rich-text posts (CKEditor) with image, video upload, and embedded YouTube video.
- Registration, login, logout, and profile with avatar upload.
- Contact form (login required) and newsletter subscription.
- Only a post's author can edit or delete it.
- Django admin at `/admin/`.

## Technology Stack

Python 3.13, Django 5.2 LTS, django-ckeditor, django-crispy-forms (bootstrap4), django-embed-video, Pillow, WhiteNoise, gunicorn; SQLite by default or PostgreSQL via `DATABASE_URL`. Frontend assets are checked-in CSS/SCSS/JS under `newssite/static/`. Versions: [VERSIONS.md](./VERSIONS.md).

## Getting Started

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/karkinirajan/web-new-nepal.git
cd web-new-nepal
export DJANGO_SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_urlsafe(50))')"
export DJANGO_DEBUG=true
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Open http://127.0.0.1:8000. All configuration is by environment variable; see [.env.example](./.env.example).

Production: set `DJANGO_DEBUG=false`, `DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS`, `DATABASE_URL` and SMTP settings, then run `migrate` and `collectstatic --noinput`. `Procfile` runs gunicorn. Do not commit secrets, local databases, or uploaded media.

## Testing

```bash
uv run pytest -q
uv run ruff check . && uv run ruff format --check .
```

Tests (`tests/`) use `newssite.settings_test` (in-memory SQLite, temp media) and cover the home/detail/category pages, author-only edit/delete, contact, newsletter, registration, login/logout and profile. CI: `.github/workflows/ci.yml`.

## Security note

`django-ckeditor` bundles CKEditor 4, which is no longer supported and has unfixed security issues (Django prints check `ckeditor.W001`). Plan a migration to a maintained editor; see work-done.md.

## Project structure

```
newssite/   settings, urls, wsgi/asgi, static assets, settings_test.py
news/       posts, categories, contact, newsletter (models, views, urls)
users/      profiles and authentication views, signals
templates/  shared and per-app templates
tests/      pytest suite
```

## License  

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.  

---

## Contributions  

Contributions are welcome! To contribute:  

1. Fork the repository.  
2. Create a feature branch:  
   ```bash  
   git checkout -b feature-name  
   ```  
3. Commit your changes:  
   ```bash  
   git commit -m "Add feature-name"  
   ```  
4. Push to your fork:  
   ```bash  
   git push origin feature-name  
   ```  
