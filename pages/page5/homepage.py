from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint
import re

# page5 blueprint definition
homepage = Blueprint('page5', __name__, static_folder='static', static_url_path='/page5', template_folder='templates')


# Routes
@homepage.route('/page5')
@homepage.route('/home')
def index():
    if session['question_num'] < 1:
        session['publisher_name'] = ['John Smith', 'Greg Williams ', 'Jacob Brown', 'Sophia Miller', 'Ava Davis',
                          'Chloe Rodriguez', 'Andrew Thomas', 'Benjamin Jackson', 'Natalie Taylor', 'Emily Perez']

        arr_ready=False

        topic1 = session['topic1']
        if topic1 == "Sport":
            ar_list=[1,2,3,4,5,6,7,8]
        if topic1 == "Politics":
            ar_list=[9,10,11,12,13,14,15,16]
        if topic1 == "Gossip":
            ar_list=[17,18,19,20,21,22,23,24]

        topic2 = session['topic2']
        if topic2 == "Sport":
            while arr_ready==False:
                rand_id = randint(1, 8)
                rand_id2 = randint(1, 8)
                if rand_id2 != rand_id:
                    ar_list.append(rand_id)
                    ar_list.append(rand_id2)
                    arr_ready=True

        if topic2 == "Politics":
            while arr_ready == False:
                rand_id = randint(9, 16)
                rand_id2 = randint(9, 16)
                if rand_id2 != rand_id:
                    ar_list.append(rand_id)
                    ar_list.append(rand_id2)
                    arr_ready = True
        if topic2 == "Gossip":
            while arr_ready == False:
                rand_id = randint(17, 24)
                rand_id2 = randint(17, 24)
                if rand_id2 != rand_id:
                    ar_list.append(rand_id)
                    ar_list.append(rand_id2)
                    arr_ready = True




        session['articles']=ar_list
        ar_list_checked = session['articles_checked']

    if session['question_num'] < 10:


            check = False
            while check == False:

                random_place_in_array=randint(0, 9)

                ar_list_checked = session['articles_checked']

                if random_place_in_array not in ar_list_checked:
                    check = True
                    ar_list_checked.append(random_place_in_array)
                    session['articles_checked'] = ar_list_checked

            articles = dbManager.fetch('select * from articles_for_facebook where new_id=%s', (session['articles'][random_place_in_array],))
            if articles:

                session['question_num'] = session['question_num'] + 1

                return render_template('homepage.html', articles=articles,article_id=articles[0], question_num=session['question_num'],publisher_name=session['publisher_name'][session['question_num']-1])



    return render_template('cq.html', final_code=session['final_id'])









@homepage.route('/homepage_insert_result',methods=['POST'])
def insert_result():

        worker_id=session['worked_id']
        article_id=request.form['article_id']
        liked=request.form['liked']
        keep_reading=0
        shared=request.form['shared']
        share_input=request.form['shared_input_to_db']
        now = datetime.now()
        print("now =", now)
        comment_input = request.form['comment_input_to_db']
        article_order_number=session['question_num']-1



        query=dbManager.commit('insert into facebook_results values (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                  (worker_id,article_id,liked,article_order_number,keep_reading,shared,share_input,now,comment_input))
        return redirect(url_for('page5.index'))
@homepage.route('/homepage_insert_no_result', methods=['POST'])
def insert_no_result():
            worker_id = session['worked_id']
            article_id1 = request.form['article_id']
            article_id= re.sub("[^0-9]", "",article_id1 )

            article_order_number = session['question_num']

            query = dbManager.commit('insert into facebook_results(worker_id,article_id,question_order) values (%s,%s,%s)',
                                     (worker_id, article_id, article_order_number))


            return redirect(url_for('page5.index'))











