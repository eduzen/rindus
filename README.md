# rindus [![Build Status](https://travis-ci.org/eduzen/rindus.svg?branch=master)](https://travis-ci.org/eduzen/rindus) [![codecov](https://codecov.io/gh/eduzen/rindus/branch/master/graph/badge.svg)](https://codecov.io/gh/eduzen/rindus)

## Django application to manage (CRUD) users and their bank account data (IBAN).

This project runs with `docker` (you can use traditional `virtualenv` but it's prepared out of the box for `docker`). We choose Django 2.0 and Python 3.6 The database is a postgresql. We use the django templates for this exercise, because it easy to manage all the app only with python. However we prefer djangorestframework and a javascript framework for a production escenario.

### Installation:

You need to install `docker` and `docker-compose` to run it. We use two images: `python 3.6` and `postgresql`. We have a `Makefile` with some rules to manage the project. Some of them are: `start`, `stop`, `dockershell`, `shell_plus`, `psql`, `migrations`. 

For example:

* To run tests and Flake8 inside of a container. Just run: 
```bash
make test
```

* To run migrations and createsuper user:
```bash
make migrate
make superuser
```

* To configure Google login.

1) Go to `localhost:8000/admin` and inside of it, go to Sites app and edit `example.com` register with `locahost:8000`. 

2) Go to https://console.developers.google.com/ and create new app and oauth2 credentials. You can follow: https://ctrlq.org/code/20353-create-application-google-apis-oauth2

3) Go back to  `localhost:8000/admin` and inside of it, go to `Social Accounts`/ `Social application` and fill it with the keys provided by google.
