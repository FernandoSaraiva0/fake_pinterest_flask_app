from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

# create the app
app = Flask(__name__)
# change string to the name of your database; add path if necessary
db_name = 'fakepinterest.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
#Secret key for forms - for security purposes
app.config['SECRET_KEY'] = "7bd3cf5ef78b72af8adf87953fd3f787"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = 'homepage'

#initialize the app with Flask-SQLAlchemy
database.init_app

#route for validate a database

@app.route('/testdb')
def testdb():
    try:
        database.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

from fakepinterest import routes

# solution for error user_loader not working
@loginManager.user_loader
def load_user(user_id):
    from fakepinterest.models import Usuario
    return Usuario.query.get(int(user_id))