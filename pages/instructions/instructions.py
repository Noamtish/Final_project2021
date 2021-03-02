from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# instructions blueprint definition
instructions = Blueprint('instructions', __name__, static_folder='static', static_url_path='/instructions', template_folder='templates')


# Routes
@instructions.route('/instructions')
def index():

    return render_template('instructions.html')



