"""This is the main application module."""
from flask import Flask

app = Flask(__name__)

# Import the views module
from . import views
