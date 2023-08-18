# login-system
## A simple login system. If the user has not yet a login account, he has to sign up, then log in with the created account. The project uses Django Framework.

# FOR A WINDOWS OPERATING SYSTEM

***

## A. Setting up development environnment

### 1. Check python version:

```
py --version
```

### 2. Check pip version 

```
py -m pip --version
```

While PIP doesn’t update often, it’s still important to stay on top of new versions for bug fixes, security fixes, and compatibility. 
To check for any upgrades, type in:

```
py -m pip install --upgrade
```

### 3. Install Django 

```
py -m pip install Django
```

### 4. Install Django-Rest-Framework

```
py -m pip install djangorestframework
```

### 5. Install Django-Cors-Headers 
To be able to link our `API` with the `Frontend`, we have to install the corsheaders module:

```
py -m pip install django-cors-headers
```
Then, edit the `login-project\login\login\settings.py` file with Application, Middleware, Trust link (From Frontend) and permission.  

## B. Execute project

### 1. In windows command propmt, go inside the project root directory and type

```
cd login 
py manage.py runserver
```

### 2. Open a browser and type:

- To Get all data       : [https://127.0.0.1:8000/api/loginsystem/](https://127.0.0.1:8000/api/loginsystem).
- To add new User       : [https://127.0.0.1:8000/api/loginsystem/signup/](https://127.0.0.1:8000/api/loginsystem/signup/).
- To edit User (Update) : [https://127.0.0.1:8000/api/loginsystem/1](https://127.0.0.1:8000/api/loginsystem/1).
  Where `1` is the `userid` and it is mandatory, that mean user info on the specified id.
  - To delete User      : [https://127.0.0.1:8000/api/loginsystem/1](https://127.0.0.1:8000/api/loginsystem/1).
  Where `1` is the `userid` and it is mandatory, that mean user info on the specified id.

## C. Execute the frontend

### 1. Go inside the frontend project

```
cd login-project
cd FrontendApp
npm install
```

### 2. Start React project

```
npm start
```

> Finally everything will be handled from the UI Frontend web App (`React`). 

## D. To create a new fresh Django website (API)

### 1. Create a Django project

```
django-admin startproject login
```

`login` is the project name.

### 2. Create Django app

```
django-admin startapp loginsystem
```

`loginsystem` is the working Django App.

### 3. Make migration to prepare the database schema

Move inside the root project by typing `cd login` from the root dir.

```
python manage.py makemigrations loginsystem
```

`loginsystem` is the working Django App. 

### 4. Create the database

```
python manage.py migrate
```

This command will create a SQLite database inside the root module.