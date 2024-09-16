Django Guide for Project
---

### 1. **Install `uv` for Speedy Development**
Before starting any Django project, install the `uv` tool, which helps streamline the installation process:

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
Activate the virtual environment to start working on your Django project:

- **For Windows**:
  ```bash
  .venv\Scripts\activate
  ```

- **For MacOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

---

### 4. **Install Django**
Once the virtual environment is activated, install Django using `uv` to ensure faster installation:

```bash
uv pip install Django
```

---

### 5. **Create a Django Project**
To start a new Django project, use the following command:

```bash
django-admin startproject project_name
```

- Replace `project_name` with your desired project name.

### 6. **Navigate into the Project Directory**
Move into your newly created project directory:

```bash
cd project_name
```

---

### 7. **Run the Django Development Server**
To run your Django development server:

- Use the default port (8000):
  ```bash
  python manage.py runserver
  ```

- Or specify a custom port (e.g., 8080):
  ```bash
  python manage.py runserver 8080
  ```

---

### 8. **Create a Django App**
To create an internal app within your project (useful for modularity), run the following command:

```bash
python manage.py startapp app_name
```

- Replace `app_name` with the desired app name.

---

### 9. **Next Steps**
After setting up the app, you can begin developing by configuring models, views, URLs, and templates based on your project requirements.

## Important Changes to setup new app

After creating new app in your Django Project makes sure below steps:
1. First create seperate templates folder for that app.
2. Create urls.py file for that app to use.
3. Add created app into settings.py file of Project in INSTALLED_APPS.
4. Add 'from django.urls import include' into urls.py file of main project to setup urls for that app seperately.
5. In the urlpatterns add 'path('url_path_name', include('app_name.urls'))' url_path_name is the path where we are going to access that app through localhost of main project.

## Important points for using funnctionalities in Project or ceated App

1. If we want to use hmtl file to render while url call we use
'from django.shortcuts import render' render is used to call that html file using 'return render(request, 'path')' path = app_name/file_name.html as app_name is not compulsory as if you are having than file to render upon call of appp route then it need to be mention.
2. We can create a layout.html file to load the data as file of reusability to use whenever same structure is got call.
dummy layout model for resusability of html code.
```
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>
        {% block title %}
            Default value
        {% endblock %}
    </title>
    <link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>
    <nav>This is Navbar</nav>
    {% block content %}{% endblock %}
</body>
</html>
```
This can be extend using below format
```
{% extends "layout.html" %}

{% block title %}
    Home Page
{% endblock %}

{% block content %}
    <h1>Main Application | Home Page</h1>
{% endblock %}
```
3. When we have to use some static content then we have to initialzie the setting.py by 'STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]' also need to 'import os' to use that static content. Using below code we can link the static file "<'link rel="stylesheet" href="{% static 'style.css' %}">" addition of ' after link is because of md file type error error.

