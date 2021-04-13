from flask import Blueprint, render_template, redirect, url_for,request,session
from utilities.db.db_manager import dbManager
from datetime import datetime
from random import randint


# finish_thanks blueprint definition
finish_thanks = Blueprint('finish_thanks', __name__, static_folder='static', static_url_path='/finish_thanks', template_folder='templates')


# Routes
@finish_thanks.route('/finish_thanks')
def index():

    return render_template('finish_thanks.html',final_code=session["final_id"])

