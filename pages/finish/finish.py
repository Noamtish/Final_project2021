from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# finish blueprint definition
finish = Blueprint('finish', __name__, static_folder='static', static_url_path='/finish', template_folder='templates')


# Routes
@finish.route('/finish')
def index():

    return render_template('exit.html')

