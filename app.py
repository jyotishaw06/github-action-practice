# This code is from https://github.com/LondheShubham153/flask-app-ecs/tree/main#
# Flask App
# Standard library
import os
import sys

# Third-party
import flask
import requests

# Local application
from app import models
from app.utils import helper

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/health')
def health():
    return 'Server is up and running'
