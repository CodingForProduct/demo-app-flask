# Intro to Frameworks & Database

Demo app done in Flask for the "Coding For Product: Intro to Frameworks & Database" lecture.


## Setup

Requirements: Anaconda Python 3, Postgres, pip

1. clone repo

2. activate a  virtual environment

conda python
```
$ conda create --name cfp_flask flask

# Mac
$ source activate cfp_flask

# Windows
$ activate cfp_demo_flask
```

3. install packages

```bash
(cfp_flask) $ pip install -r requirements
```

4. create database

```bash
(cfp_flask) $ createdb <database_name>
```

5.  set up enviroment variables
- copy .env.sample, and rename it .env
- fill in the `DATABASE_URI`

6. run migrations

```bash
(cfp_flask) $ python manage.py db upgrade

```

7. run seed data to populate database
```bash
(cfp_flask) $ python manage.py seed
```
## Start application

(cfp_flask) $ python3 app.py
