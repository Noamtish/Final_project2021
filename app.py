from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## exit
from pages.exit.exit import exit
app.register_blueprint(exit)

## declaration
from pages.declaration.declaration import declaration
app.register_blueprint(declaration)

## instructions
from pages.instructions.instructions import instructions
app.register_blueprint(instructions)



## finish
from pages.finish.finish import finish
app.register_blueprint(finish)

## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

##adadadsad