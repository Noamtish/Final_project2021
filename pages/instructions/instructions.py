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



@instructions.route('/instructions_to_homepage',methods=['GET','post'])
def update_final_key():
    session['worked_id']=request.args['worker_id']
    worked_id=session['worked_id']
    final_id=request.args['worker_id']+"777BGU"
    session['final_id']=final_id
    device=request.args['device']

    query = dbManager.commit('insert into Pretest_users values (%s,%s)',
                             (worked_id,device))


    return redirect(url_for('homepage.index'))



