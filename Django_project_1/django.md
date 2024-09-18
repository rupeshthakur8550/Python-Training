# Django Guide for Project Setup

---

### 1. **Install `uv` for Efficient Development**
Before starting any Django project, install the `uv` tool to streamline the installation process:

```bash
pip install uv
```

---

### 2. **Set Up a Virtual Environment**
A virtual environment isolates the project’s dependencies. Use `uv` to create a virtual environment:

```bash
uv venv
```

### 3. **Activate the Virtual Environment**
Activate the virtual environment to work on your Django project:

- **For Windows**:
  ```bash
  .venv\Scripts\activate
  ```

- **For macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

---

### 4. **Install Django**
Once the virtual environment is activated, install Django using `uv` for faster installation:

```bash
uv pip install Django
```

---

### 5. **Create a Django Project**
To start a new Django project, use the following command:

```bash
django-admin startproject project_name
```

Replace `project_name` with your desired project name.

### 6. **Navigate to the Project Directory**
Move into your newly created project directory:

```bash
cd project_name
```

---

### 7. **Run the Django Development Server**
To run your Django development server, use the following command:

- For the default port (8000):
  ```bash
  python manage.py runserver
  ```

- To specify a custom port (e.g., 8080):
  ```bash
  python manage.py runserver 8080
  ```

---

### 8. **Create a Django App**
To create an internal app within your project (useful for modularity), run:

```bash
python manage.py startapp app_name
```

Replace `app_name` with your desired app name.

---

### 9. **Next Steps**
After setting up your app, begin developing by configuring models, views, URLs, and templates based on your project requirements.

## Important Steps for Setting Up a New App

After creating a new app in your Django project, follow these steps:

1. Create a separate `templates` folder for the app.
2. Create a `urls.py` file for the app.
3. Add the created app to the `INSTALLED_APPS` list in the `settings.py` file of the project.
4. Include `from django.urls import include` in the main project's `urls.py` file to set up URLs for the app separately.
5. In the `urlpatterns`, add `path('url_path_name', include('app_name.urls'))` to access the app through the main project.

## Key Points for Using Functionalities in Your Project or App

1. To render an HTML file when a URL is called, use:
   ```python
   from django.shortcuts import render
   return render(request, 'path/to/template.html')
   ```
   Here, `path` is the location of your template file. Including the app name is optional unless needed.

2. Create a `layout.html` file for reusable HTML structure. Here's a simple layout example:
   ```html
   {% load static %}
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>{% block title %}Default value{% endblock %}</title>
       <link rel="stylesheet" href="{% static 'style.css' %}">
   </head>
   <body>
       <nav>This is Navbar</nav>
       {% block content %}{% endblock %}
   </body>
   </html>
   ```

   You can extend this layout in other templates like this:
   ```html
   {% extends "layout.html" %}

   {% block title %}
       Home Page
   {% endblock %}

   {% block content %}
       <h1>Main Application | Home Page</h1>
   {% endblock %}
   ```

3. To use static content, initialize the `settings.py` with:
   ```python
   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
   ```
   Ensure you also import `os` at the top of your `settings.py` file. Link static files in your templates as follows:
   ```html
   <link rel="stylesheet" href="{% static 'style.css' %}">
   ```

## Tailwind CSS Installation Guide

1. Install `pip` if not already done:
   ```bash
   python -m ensurepip --upgrade
   ```

2. Run the following commands to install Tailwind CSS in your virtual environment:
   ```bash
   pip install django-tailwind
   pip install 'django-tailwind[reload]'
   ```

3. Add `'tailwind'` to your main project's `settings.py` under `INSTALLED_APPS`:
   ```python
   INSTALLED_APPS = [
       # ...
       'tailwind',
       # ...
   ]
   ```

4. Initialize the Tailwind app (default name: `theme`):
   ```bash
   python manage.py tailwind init
   ```

5. Add the created app to your `settings.py` with the following modifications:
   ```python
   INSTALLED_APPS = [
       # ...
       'theme',
       # ...
   ]

   TAILWIND_APP_NAME = 'theme' 
   INTERNAL_IPS = ['127.0.0.1']
   
   NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
   ```

6. Generate the necessary files for Tailwind:
   ```bash
   python manage.py tailwind install
   ```

7. You will need two terminal windows: one for running the server and another for Tailwind.

   First terminal:
   ```bash
   python manage.py runserver
   ```

   Second terminal:
   ```bash
   python manage.py tailwind start
   ```

8. To automatically reload the page without refreshing it each time, add the following to your `settings.py`:
   ```python
   INSTALLED_APPS = [
       # ...
       'django_browser_reload',
       # ...
   ]

   MIDDLEWARE = [
       # ...
       "django_browser_reload.middleware.BrowserReloadMiddleware",
       # ...
   ]
   ```

9. Finally, add the following to the `urls.py` file of your main project:
   ```python
   from django.urls import include, path

   urlpatterns = [
       # ...
       path("__reload__/", include("django_browser_reload.urls")),
   ]
   ```
