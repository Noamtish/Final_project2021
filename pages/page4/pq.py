from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# exit blueprint definition
pq = Blueprint('pq', __name__, static_folder='static', static_url_path='/pq', template_folder='templates')


# Routes
@pq.route('/pq')
def index():

    return render_template('pq.html')



@pq.route('/interests_after_pick')
def choose_topics():
    session['topic1'] = request.args["topic1"]
    session['topic2'] = request.args["topic2"]

    return redirect(url_for('page5.index'))