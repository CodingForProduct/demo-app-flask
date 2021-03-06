import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__), ".env"))

DEBUG = os.environ.get("DEBUG")
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
