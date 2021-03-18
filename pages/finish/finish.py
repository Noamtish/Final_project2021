from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# finish_thanks blueprint definition
finish = Blueprint('finish', __name__, static_folder='static', static_url_path='/finish', template_folder='templates')


# Routes
@finish.route('/finish')
def index():
    device = request.args['device']
    worked_id = session['worked_id']


    query = dbManager.commit('insert into Pretest_users values (%s,%s)',
                             (worked_id, device))

    return render_template('finish_thanks.html',final_code=session["final_id"])

