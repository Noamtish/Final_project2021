from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# fc blueprint definition
fc = Blueprint('fc', __name__, static_folder='static', static_url_path='/fc', template_folder='templates')


# Routes
@fc.route('/')
def index():

    return render_template('fc.html')

