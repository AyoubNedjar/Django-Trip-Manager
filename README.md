# Django Trip Manager

A Django web application developed in Python for managing trips and reservations. This application includes an admin interface for handling drivers, clients, routes, and reservations efficiently.

## Table of Contents
1. [Requirements](#requirements)
2. [Setup](#setup)
3. [Project Creation](#project-creation)
4. [Running the Application](#running-the-application)
5. [Usage](#usage)
6. [License](#license)

## Requirements

- Python 3.x
- Django

## Setup

1. **Create a virtual environment:**

    ```bash
    python -m venv .venv
    ```

2. **Activate the virtual environment:**

    **On Windows:**
    ```bash
    Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
    .\.venv\Scripts\activate
    ```

    **On macOS/Linux:**
    ```bash
    source .venv/bin/activate
    ```

3. **Install Django and other dependencies:**

    ```bash
    pip install django
    pip install ipython
    ```

4. **Freeze the installed packages into `requirements.txt`:**

    ```bash
    pip freeze > requirements.txt
    ```

## Project Creation

1. **Start a new Django project:**

    ```bash
    python -m django startproject nomProjet
    ```

2. **Navigate into the project directory:**

    ```bash
    cd nomProjet
    ```

3. **Create a new Django app:**

    ```bash
    python manage.py startapp nomApp
    ```

4. **Add the new app to `settings.py`:**

    Open `nomProjet/settings.py` and add `'nomApp.apps.NomAppConfig',` to the `INSTALLED_APPS` list.

5. **Make migrations for the new app:**

    ```bash
    python manage.py makemigrations nomApp
    ```

6. **Apply the migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Create a superuser for admin access:**

    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## Usage

1. **Access the admin interface:**

    Open a web browser and go to `http://127.0.0.1:8000/admin` to log in with the superuser credentials you created.

2. **Manage your trips and reservations:**

    Use the admin interface to add, edit, and manage drivers, clients, routes, and reservations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
