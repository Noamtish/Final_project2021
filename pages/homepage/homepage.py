from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/homepage')
@homepage.route('/home')
def index():

    if session['question_num']<15:
        check = False
        while check == False:
            rand_id = randint(1, 60)
            ar_list = session['articles_checked']


            if rand_id not in ar_list:
                check = True
        ar_list.append(rand_id)
        session['articles_checked'] = ar_list

        articles = dbManager.fetch('select * from articles where id=%s', (rand_id,))



        if articles:
            session['question_num'] =session['question_num']+1
            return render_template('homepage.html', articles=articles,question_num=session['question_num'])

        return render_template('homepage.html')

    return render_template('finish.html',final_code=session['final_id'])









@homepage.route('/homepage_insert_result',methods=['POST'])
def insert_result():

        worker_id=session['worked_id']
        article_id=request.form['article_id']
        article_novelty_rank = request.form['article_novelty_rank']
        article_outrage_rank = request.form['article_outrage_rank']
        article_refuted_rank = request.form['article_refuted_rank']
        now = datetime.now()
        print("now =", now)



        query=dbManager.commit('insert into Pretest_result values (%s,%s,%s,%s,%s)',
                                 (article_id,'novelty',article_novelty_rank,now,worker_id))
        query = dbManager.commit('insert into Pretest_result values (%s,%s,%s,%s,%s)',
                                 (article_id,'outrage', article_outrage_rank, now,worker_id))
        query = dbManager.commit('insert into Pretest_result values (%s,%s,%s,%s,%s)',
                                 (article_id,'refuted', article_refuted_rank, now,worker_id))


        return redirect(url_for('homepage.index'))











