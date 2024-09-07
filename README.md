Django Trip Manager
A Django web application developed in Python for managing trips and reservations. This application includes an admin interface for handling drivers, clients, routes, and reservations efficiently.

Table of Contents
Requirements
Setup
Project Creation
Running the Application
Usage
License
Requirements
Python 3.x
Django
Setup
Create a virtual environment:

bash
Copier le code
python -m venv .venv
Activate the virtual environment:

On Windows:

bash
Copier le code
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
.\.venv\Scripts\activate
On macOS/Linux:

bash
Copier le code
source .venv/bin/activate
Install Django and other dependencies:

bash
Copier le code
pip install django
pip install ipython
Freeze the installed packages into requirements.txt:

bash
Copier le code
pip freeze > requirements.txt
Project Creation
Start a new Django project:

bash
Copier le code
python -m django startproject nomProjet
Navigate into the project directory:

bash
Copier le code
cd nomProjet
Create a new Django app:

bash
Copier le code
python manage.py startapp nomApp
Add the new app to settings.py:

Open nomProjet/settings.py and add 'nomApp.apps.NomAppConfig', to the INSTALLED_APPS list.

Make migrations for the new app:

bash
Copier le code
python manage.py makemigrations nomApp
Apply the migrations:

bash
Copier le code
python manage.py migrate
Create a superuser for admin access:

bash
Copier le code
python manage.py createsuperuser
Run the development server:

bash
Copier le code
python manage.py runserver
Usage
Access the admin interface:

Open a web browser and go to http://127.0.0.1:8000/admin to log in with the superuser credentials you created.

Manage your trips and reservations:

Use the admin interface to add, edit, and manage drivers, clients, routes, and reservations.

License
This project is licensed under the MIT License - see the LICENSE file for details.