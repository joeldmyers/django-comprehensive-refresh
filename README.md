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

This creates a blog. 

To include routes from a sub-project we need to import the include from django.urls, and include it like this: 

`path('blog/',  include('blog.urls'))`

We need to make a folder within the templates folder with the same name as the current app to let Django know these are for the correct app. 

We need to add the Blog in settings.py to the list of installed apps

To use a template that we can extend, do this:

`{% block content %}{% endblock %}`

Then in the file, do 

`{% extends "blog/base.html" %}`

then... 

```
  {% block content %}
  {% endblock content %}
```

We keep static files in a folder called 'static/PROJECT_NAME'