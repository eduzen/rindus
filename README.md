# rindus [![Build Status](https://travis-ci.org/eduzen/rindus.svg?branch=master)](https://travis-ci.org/eduzen/rindus) [![codecov](https://codecov.io/gh/eduzen/rindus/branch/master/graph/badge.svg)](https://codecov.io/gh/eduzen/rindus)

Django application to manage (CRUD) users and their bank account data (IBAN).


This project runs with docker (you can use traditional virtualenv but it's prepared out of the box for docker)

So you need docker and docker-compose to run it. We use two images: python 3.6 and postgresql

We have a `Makefile` with some rules for easy use:

* Flake8 and Tests
`make test`

* Run migrations and createsuper user:
```
make migrate
make superuser
```
