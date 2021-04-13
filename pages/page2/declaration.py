from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# page2 blueprint definition
declaration = Blueprint('page2', __name__, static_folder='static', static_url_path='/page2', template_folder='templates')


# Routes
@declaration.route('/page2')
def index():
    session['worked_id'] = request.args['worker_id']

    final_id = request.args['worker_id'] + "777BGU"
    session['final_id'] = final_id
    session['articles_checked'] = []
    session['question_num']=0
    return render_template('declaration.html')

