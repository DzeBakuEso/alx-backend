# 0x02. i18n

## 📌 Project Overview
This project focuses on implementing internationalization (i18n) in a Flask web application using the Flask-Babel extension. It demonstrates how to display content in multiple languages, infer the appropriate locale from various sources, and localize timestamps based on user settings or request context.

> **Duration**: May 19, 2025 6:00 PM → May 20, 2025 6:00 PM  
> **Weight**: 1  
> **Checker Release**: May 20, 2025 12:00 AM  
> **Manual QA Review Required**

---

## 🧠 Learning Objectives
- Parametrize Flask templates for different languages.
- Infer the correct locale from URL parameters, user settings, or request headers.
- Localize timestamps using user-preferred time zones.

---

## 📚 Resources
- [Flask-Babel Documentation](https://python-babel.github.io/flask-babel/)
- [Flask i18n Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz Timezones](https://pytz.sourceforge.net/)

---

## ⚙️ Requirements
- All code is written in **Python 3.7**.
- Tested on **Ubuntu 18.04 LTS**.
- All Python files end with a new line and are **executable**.
- Follows **pycodestyle** (version 2.5).
- Documentation for all modules, classes, and methods.
- Functions and coroutines are **type-annotated**.
- First line of all Python files: `#!/usr/bin/env python3`
- `README.md` file is mandatory.

---

## 🚀 Project Structure & Tasks

### `0-app.py`
> **Task 0: Basic Flask App**  
- A basic Flask app with a single route `/` displaying:
  - `<title>Welcome to ALX</title>`
  - `<h1>Hello world</h1>`

### `1-app.py`
> **Task 1: Basic Babel Setup**  
- Installed Flask-Babel (`flask_babel==2.0.0`)
- Created `Config` class with:
  - `LANGUAGES = ['en', 'fr']`
  - Default locale: `en`
  - Default timezone: `UTC`

### `2-app.py`
> **Task 2: Get Locale from Request**  
- Added `get_locale()` function with `babel.localeselector` to detect the best match from `request.accept_languages`.

### `3-app.py`
> **Task 3: Parametrize Templates**  
- Used `_()`/`gettext()` for translations.
- Added `babel.cfg` and initialized translations.
- Created `.po` and compiled `.mo` files for:
  - English (en)
  - French (fr)

### `4-app.py`
> **Task 4: Force Locale with URL Parameter**  
- Modified `get_locale()` to check `locale` in URL query string.
- Allows forcing a specific locale like `/index?locale=fr`.

### `5-app.py`
> **Task 5: Mock Logging In**  
- Simulated login using `login_as` query parameter.
- Set current user in `flask.g.user`.
- Displayed user-specific message based on login status.

### `6-app.py`
> **Task 6: Use User Locale**  
- Updated `get_locale()` to prioritize:
  1. URL parameter
  2. User settings (`user["locale"]`)
  3. Request headers
  4. Default locale

### `7-app.py`
> **Task 7: Infer Appropriate Timezone**  
- Created `get_timezone()` with `babel.timezoneselector`.
- Timezone priority:
  1. URL parameter
  2. User setting (`user["timezone"]`)
  3. Default: `UTC`
- Used `pytz.timezone()` with exception handling for validation.

---

## 🛠️ How to Run

1. Install dependencies:
   ```bash
   pip3 install flask flask_babel pytz

Author: Dzeble Kwame Baku
