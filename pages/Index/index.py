from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# index blueprint definition
index = Blueprint('index', __name__, static_folder='static', static_url_path='/index', template_folder='templates')


# Routes
@index.route('/')
def index():

    return render_template('index.html')

