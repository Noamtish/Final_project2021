from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# declaration blueprint definition
declaration = Blueprint('declaration', __name__, static_folder='static', static_url_path='/declaration', template_folder='templates')


# Routes
@declaration.route('/')
def index():
    session['articles_checked'] = []
    session['question_num']=0
    return render_template('declaration.html')

