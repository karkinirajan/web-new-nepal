# Work done: web-new-nepal

Branch: `chore/modernize` (local, not pushed). Date: 2026-10-29.

## What was there
A Django 3.1 news site (apps `news`, `users`, project `newssite`) with 2020-2021 pins (58 packages, many unused), Heroku-style deployment, only empty `tests.py` stubs. Tracked in git: `db.sqlite3`, `.pyc` files, 57 uploaded media files, `.vscode/settings.json`, and 1,586 static asset files (source CSS/SCSS/JS/fonts/images, kept).

## Step 1: your uncommitted work, committed as-is
- `newssite/settings.py`: secret key, DEBUG, ALLOWED_HOSTS, and email credentials moved to environment variables.
- `README.md`: corrected prerequisites (no npm build exists), setup and production notes.
- `.gitignore` added; `db.sqlite3` and bytecode removed from tracking.

## Step 2: modernization changes by file
| File | Before | Change |
|---|---|---|
| `pyproject.toml`, `uv.lock`, `.python-version` | absent | New uv project, Python 3.13, Django 5.2 LTS; only the dependencies the code uses |
| `requirements.txt`, `runtime.txt` | 58 old pins | Exported from lockfile (Heroku-style builds); python-3.13 |
| `newssite/settings.py` | `django_heroku`, `USE_L10N`, unused `django_filters` app, fixed SQLite | Removed those; `DATABASE_URL` via dj-database-url; `STORAGES` with WhiteNoise; crispy bootstrap4 pack; CSRF trusted origins; HTTPS/HSTS/secure cookies when not debug |
| `newssite/settings_test.py` | absent | New test settings |
| `news/views.py` | `PostCreateView` built an unused `EmailMessage` at import with a hardcoded personal address; `subscribe` raised on GET (returned None) and on anonymous POST without `user_id` | Dead email object (and its two imports) removed; `subscribe` redirects on GET, tolerates missing `user_id`, one duplicate check |
| `news/models.py` | `Contact.contact_date` default `datetime.now` (naive); `Youtube`, `Comment`, `Like` had no `__str__` | `timezone.now`; added `__str__` methods |
| `news/migrations/0020_alter_contact_contact_date.py` | absent | New |
| `news/forms.py` | `fields = "__all__"` | Explicit field list (same fields) |
| `news/apiviews.py` (not routed anywhere) | `from .models import *`; `request.is_ajax` (removed in Django 4) | Explicit imports; the `is_ajax` guard replaced by `if True:` with a comment. File remains unrouted |
| `users/models.py` | `Profile.save()` crashed if the avatar file is missing (`default.jpg`) | Skip resize when file absent |
| `users/apps.py` | `ready()` imports signals | Kept (with noqa) after ruff's autofix removed it and the tests caught the broken profile creation |
| `news/tests.py`, `users/tests.py` | empty stubs | Deleted; `tests/` has 31 tests |
| other `.py` files | mixed formatting | `ruff format` and import sort only |
| `.github/workflows/ci.yml`, `.env.example` | absent | New |
| `.gitignore` | had basics | Also ignores `.vscode/` and caches |
| `media/` (57 files), `.vscode/` | tracked | Untracked with `git rm --cached`; files remain on disk |
| `README.md` | generic feature list and an npm build that does not exist | Rewritten to match the code |
| `VERSIONS.md`, `work-done.md` | absent | New |

## Verification (actual runs)
- `uv run pytest -q`: 31 passed (all 13 category pages render).
- `uv run ruff check .` and `ruff format --check .`: clean.
- `makemigrations --check --dry-run`: no changes; the full migration chain applies on a fresh SQLite DB.
- `manage.py check` reports one warning, `ckeditor.W001` (see below); intentionally not silenced.
- `check --deploy` not run for this repo.

## Needs your attention
- **Security: CKEditor 4.** `django-ckeditor` ships CKEditor 4.22.1, unsupported, with unfixed security issues, and posts store rich HTML. Replacing it (for example with `django-ckeditor-5`, subject to its license) changes the field type and should be a separate, tested change. I did not do it.
- **Rotate credentials** that were committed in earlier history (old secret key and email settings), and consider a history rewrite; `db.sqlite3` and media files are also in history.
- Not changed: `news/apiviews.py` (likes/comments JSON endpoints) is not routed in `urls.py`; the templates may expect them. `PostCreateView` uses `fields = "__all__"` (shows the author field).
- Nothing pushed. To publish: `git push -u origin chore/modernize`
