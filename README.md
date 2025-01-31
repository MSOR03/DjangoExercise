# Django Project Setup Guide

This guide will walk you through creating a Django project from scratch and running it locally.

## Prerequisites

Ensure you have the following installed:
- Python (>=3.8)
- pip (Python package manager)
- Git (optional, for version control)


### Step 1: Install Django

```sh
pip install django
```

### Step 2: Create a Django Project

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


