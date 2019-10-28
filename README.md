# django-comprehensive-refresh

Create a virtual env first. 

First command: `django-admin startproject joels_project` gives us a new project.  

This creates the core files: 

__init__.py
settings.py - db, etc.
urls.py - routes. 
wsgi.py - how Python and the web server communicate.  Pronounced almost like whiskey.  
manage.py - the file that lets us run command line commands.

Then go into joels_project and use

`python manage.py runserver`

http://127.0.0.1:8000/ now website is up!

## Creating a blog app

Generally Django can have multiple apps within the same project. 

`python manage.py startapp blog`

This creates a blog