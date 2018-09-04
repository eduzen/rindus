# rindus [![Build Status](https://travis-ci.org/eduzen/rindus.svg?branch=master)](https://travis-ci.org/eduzen/rindus) [![codecov](https://codecov.io/gh/eduzen/rindus/branch/master/graph/badge.svg)](https://codecov.io/gh/eduzen/rindus)

## Django application to manage (CRUD) users and their bank account data (IBAN).

This project runs with `docker` (you can use traditional `virtualenv` but it's prepared out of the box for `docker`). We choose `Django 2.0` and `Python 3.6` The database is a `postgresql`. We use the django templates for this exercise, because it easy to manage all the app only with `python`. However we prefer `django-rest-framework` and a `javascript framework` for a production escenario.

### Requirements:

You need to install `docker` and `docker-compose` to run it. We use two images: `python 3.6` and `postgresql`. We have a `Makefile` with some rules to manage the project. Some of them are: `start`, `stop`, `dockershell`, `shell_plus`, `psql`, `migrations`.

#### For example:

* To run tests and Flake8 inside of a container. Just run:
```bash
make test
```

### Configuration:

* To start the project just run:
```bash
make start
```
This command will pull docker images and run them inside of a container.

* Then you need to setup the database and create a superuser. We have two targets:
```bash
make migrate
make superuser
```

* For google accounts, you need to configure the "Google login".

1) Go to `localhost:8000/admin` and inside of it, go to Sites app:

![Image](docs/sites.png?raw=true)

and edit `example.com` register with `locahost:8000` like this img:

![Image](docs/localhost.png?raw=true)

You can choose a diffent domain name if you want to deploy it in VM.

2) Go to https://console.developers.google.com/ and create new app and oauth2 credentials.
You can follow [this instructions](https://ctrlq.org/code/20353-create-application-google-apis-oauth2)

3) Go back to  `localhost:8000/admin` and inside of it, go to `Social Accounts`/ `Social application` and fill it with the keys provided by google.
![Image](docs/social.png?raw=true)

* Now, You can use the app going to `http://localhost:8000/`:
![Image](docs/googlelogin.png?raw=true)

* See list of users, edit and delete them `http://localhost:8000/`:
![Image](docs/listofuser.png?raw=true)

* Create users `http://localhost:8000/user/add`:
![Image](docs/createuser.png?raw=true)

* Edit users `http://localhost:8000/user/<:id>`:


