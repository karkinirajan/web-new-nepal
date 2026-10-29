# Web News Nepal

## Overview  

**webNewsNepal** is a Django news publishing site with category pages, user accounts, media uploads, and an admin interface.

---

## Features  

- **News Management**:  
  - Add, edit, and delete news articles.  
  - Categorize articles for better organization.  

- **Responsive Design**:  
  - Fully optimized for desktops, tablets, and mobile devices.  

- **Modern User Interface**:  
  - Built with SCSS and CSS for a polished and visually appealing design.  

- **Dynamic Functionality**:  
  - Interactive features powered by JavaScript.  

- **Backend Integration**:  
  - Python-based backend for server-side functionality.  

---

## Technology Stack  

- **Frontend**: JavaScript, CSS, SCSS, HTML  
- **Backend**: Python  

---

## Getting Started  

### Prerequisites  

Ensure Python and pip are installed. The checked-in stylesheets and scripts are served as static files; this repository has no `package.json` or npm build step.

### Installation  

1. Clone the repository:  
   ```bash  
   git clone https://github.com/karkinirajan/web-new-nepal.git
   cd web-new-nepal
   ```  

2. Create and activate a virtual environment for the backend:  
   ```bash  
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```  

3. Install backend dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

4. Set a unique local secret and enable debug mode for local development:
   ```bash
   export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
   export DJANGO_DEBUG=true
   export DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
   ```
5. Create the local database and an admin account:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Start the backend server with `python manage.py runserver` and open
   `http://127.0.0.1:8000`.

Production deployments must set `DJANGO_DEBUG=false`, configure
`DJANGO_ALLOWED_HOSTS`, and provide a database through `DATABASE_URL`. Configure
email with `DJANGO_EMAIL_HOST`, `DJANGO_EMAIL_PORT`, `DJANGO_EMAIL_HOST_USER`,
`DJANGO_EMAIL_HOST_PASSWORD`, and `DJANGO_EMAIL_USE_TLS`. Email defaults to the
console backend locally. Do not commit secrets, local databases, or uploaded media.

---

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
