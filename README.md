# Django Project Setup Guide

This guide will walk you through creating a Django project from scratch and running it locally.

## Prerequisites

Ensure you have the following installed:
- Python (>=3.8)
- pip (Python package manager)
- virtualenv (recommended)
- Git (optional, for version control)

## 1. Setting Up the Django Project

### Step 1: Create a Virtual Environment
It's best practice to use a virtual environment to manage dependencies:

```sh
python -m venv venv
```

Activate the virtual environment:
- **Windows:**
  ```sh
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```sh
  source venv/bin/activate
  ```

### Step 2: Install Django

```sh
pip install django
```

### Step 3: Create a Django Project

Run:

```sh
django-admin startproject myproject
```

This will create a folder named `myproject` with the basic Django project structure.

### Step 4: Navigate into the Project Folder

```sh
cd myproject
```

## 2. Running the Django Server

To start the development server, run:

```sh
python manage.py runserver
```

This will start the server at:

```
http://127.0.0.1:8000/
```

You should see the default Django welcome page.

## 3. Creating a Django App

Django projects are made up of apps. To create an app inside your project:

```sh
python manage.py startapp myapp
```

Now, register the app in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'myapp',
]
```

## 4. Applying Migrations

Django uses migrations to manage database changes. Run:

```sh
python manage.py migrate
```

## 5. Creating a Superuser (For Admin Panel)

To create an admin user:

```sh
python manage.py createsuperuser
```

Enter the required details (username, email, and password), then log in at:

```
http://127.0.0.1:8000/admin/
```

## 6. Running the Project in a Different Port

By default, Django runs on port `8000`. You can change it like this:

```sh
python manage.py runserver 8080
```

This will run the server at:

```
http://127.0.0.1:8080/
```

## 7. Deactivating the Virtual Environment

When you're done, deactivate the virtual environment:

```sh
deactivate
```

---

## Additional Resources

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)

Happy coding! 🚀
