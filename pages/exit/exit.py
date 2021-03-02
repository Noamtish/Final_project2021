from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# exit blueprint definition
exit = Blueprint('exit', __name__, static_folder='static', static_url_path='/exit', template_folder='templates')


# Routes
@exit.route('/exit')
def index():

    return render_template('exit.html')

