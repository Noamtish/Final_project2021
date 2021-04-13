from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# page3_cf blueprint definition
instructions = Blueprint('page3_cf', __name__, static_folder='static', static_url_path='/page3_cf', template_folder='templates')


# Routes
@instructions.route('/page3_cf')
def index():

    return render_template('instructions.html')



@instructions.route('/instructions_to_homepage',methods=['GET','post'])
def update_final_key():
    # session['worked_id']=request.args['worker_id']

    # final_id=request.args['worker_id']+"777BGU"
    # session['final_id']=final_id
    # device=request.args['device']
    #
    # query = dbManager.commit('insert into Pretest_users values (%s,%s)',
    #                          (worked_id,device))


    return redirect(url_for('pq.index'))



