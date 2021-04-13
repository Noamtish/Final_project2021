from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# exit blueprint definition
cq = Blueprint('cq', __name__, static_folder='static', static_url_path='/cq', template_folder='templates')


# Routes
@cq.route('/cq')
def index():

    return render_template('cq.html')


@cq.route('/cq_insert_result',methods=['POST'])
def insert_result():
    worker_id = session['worked_id']
    age=request.form['age']
    topic1=session['topic1']
    topic2=session['topic2']
    gender = request.form['Gender']
    Education_level= request.form['Education level']
    computer_use = request.form['computer use']
    mobile_use = request.form['mobile use']
    political_view = request.form['political view']
    device = request.form['device']
    place_size=request.form['place_size']
    level_of_privacy=request.form['level_of_privacy']
    level_of_confined_space=request.form['level_of_confined_space']
    level_of_noise=request.form['level_of_noise']
    level_of_light=request.form['level_of_light']
    level_of_croweded_env=request.form['level_of_croweded_env']


    query=dbManager.commit('insert into facebook_users values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                             (worker_id,device,topic1,topic2,age,gender,Education_level,computer_use,mobile_use,political_view ,place_size,level_of_privacy,level_of_confined_space,level_of_noise,level_of_light,level_of_croweded_env))

    return redirect(url_for('finish_thanks.index'))