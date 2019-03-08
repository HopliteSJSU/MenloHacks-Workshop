## :wrench: MenloHacks Workshop :hammer:

This is the repo for the Django to-do-list app Workshop in MenloHacks 2019 on Saturday March 9th.
It gives the overview about how to set up a simple Django project. This workshop is beginners-friendly.

## Installation
* Python
* Pip (Python Package Installer)
* Django (Open Source Web Application Framework)
* Git (Open Source Distributed Version Control System)

### Step 1 - Check Python Installation<br/>
`$ python3 --version`

### Step 2 - Check pip Installation<br>
`$ pip3 --version`

  #### If pip not installed
  **macOS**:  
  `$ brew install python`  
  <br />
  **Windows**:  
  [Download here](https://www.python.org/downloads/release/python-372/)

### Step 3 - Django Installation
`$ pip3 install Django`

Check your Django Installation<br><br>
Access Python by:`$ python` or `$ python3`. Then:<br>
`>>> import django`<br>
`>>> print(django.get_version())`<br>

### Step 4 - Git Clone This Repo
`git clone`

### Step 5 - Access to the Folder
`cd django-to-do-list`<br>
#### Folder hierarchy<br>
```
django-to-do-list
├───db.sqlite3
├───manage.py
├───todo_app (back-end)
│        settings.py
│        urls.py
│        wsgi.py
│        __init__.py
│        .....
├───todo_list (front-end)
│        settings.py
│        urls.py
│        wsgi.py
│        __init__.py
│        .....
└───README.md
```

### Step 6 - Usage
`python3 manage.py runserver`

#### Go to
`http://localhost:8000`

## Credits

#### Bruce Lin (https://github.com/brucelin1218)
#### Tim Roesner (https://github.com/timroesner)

