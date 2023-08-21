# login-system

### A simple login system. If the user has not yet a login account, he has to sign up, then log in with the created account. The project uses Django Framework.

# Steps to follow

---

## A. Setting up development environnment

### 1. Check python version:

```
python --version
```

### 2. Check pip version

```
pip --version
```

While PIP doesn’t update often, it’s still important to stay on top of new versions for bug fixes, security fixes, and compatibility.
To check for any upgrades, type in:

```
python -m pip install --upgrade
```

### 3. Install Django

```
pip install Django
```

### 4. Install Django Rest Framework

```
pip install djangorestframework
```

### 5. Install Django corsheaders

To be able to link our `API` with the `Frontend`, we have to install the corsheaders module:

```
pip install django-cors-headers
```

Then, edit the `login-project\login\login\settings.py` file with Application, Middleware, Trust link (From Frontend) and permission.

## B. Execute project

### 1. In windows command propmt, go inside the project root directory and type

```
cd backendApp
python manage.py runserver
```

### 2. Open a browser and type:

- To get all Users | add User : [https://127.0.0.1:8000/api/loginsystem/](https://127.0.0.1:8000/api/loginsystem/).
- To edit or update | delete User : [https://127.0.0.1:8000/api/loginsystem/1/](https://127.0.0.1:8000/api/loginsystem/1/).
  Where `1` is the `userid` and it is mandatory, that means user's info on the specified id.

## C. Execute the frontend

### 1. Go inside the project root directory and type

```
cd frontendApp
cd login-system-app
npm install
```

### 2. Start React project

```
npm start
```

> Finally, we can view the `Django REST API Data` throught the `React Frontend UI`.

## D. Creating a fresh Django website (API)

### 1. Create a Django project

```
django-admin startproject backendApp
```

`backendApp` is the project name.

### 2. Create Django app

```
django-admin startapp loginsystem
```

`loginsystem` is the working Django App.

### 3. Make migrations to prepare the database schema

Move inside the root project by typing `cd backendApp` from the root dir.

```
python manage.py makemigrations loginsystem
```

`loginsystem` is the working Django App.

### 4. Create the database

```
python manage.py migrate
```

This command will create a `SQLite database` inside the root module.

## E. App outputs

### 1. Add new data

![1-REST-API-Add data](https://github.com/josamuna/login-project/assets/15903230/97ad30cf-1f4d-42bd-85fc-eaf772180784)

### 2. Fetch, Update and Delete data

![2-REST-API-Feach Update Delete data](https://github.com/josamuna/login-project/assets/15903230/3be1f972-ff25-4d8e-9503-e05e36ccc4a7)

### 3. Data deleted

![3-REST-API-Data Deleted](https://github.com/josamuna/login-project/assets/15903230/4ab2974a-ea60-4404-83f7-6777a553c6b5)

### 4. Showing data from React frontend App

![4-Showing data from React App](https://github.com/josamuna/login-project/assets/15903230/ae8ac509-685d-4839-8fd5-5368be913422)
