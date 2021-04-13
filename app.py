from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## exit
from pages.exit.exit import exit
app.register_blueprint(exit)



## page2
from pages.page2.declaration import declaration
app.register_blueprint(declaration)



## page3_cf
from pages.page3_cf.instructions import instructions
app.register_blueprint(instructions)

## finish_thanks
from pages.finish_thanks.finish_thanks import finish_thanks
app.register_blueprint(finish_thanks)

## Homepage
from pages.page5.homepage import homepage
app.register_blueprint(homepage)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

## Page characteristics questionnaire
from pages.page6.cq import cq
app.register_blueprint(cq)

## Page first code
from pages.page1.fc import fc
app.register_blueprint(fc)

## Page preferences questionnaire
from pages.page4.pq import pq
app.register_blueprint(pq)

###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

##adadadsad