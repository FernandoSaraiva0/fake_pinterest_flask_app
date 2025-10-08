from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fakepinterest.db'
app.config['SECRET_KEY'] = "7bd3cf5ef78b72af8adf87953fd3f787"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = 'homepage'

from fakepinterest import routes

# solution for error user_loader not working
@loginManager.user_loader
def load_user(user_id):
    from fakepinterest.models import Usuario
    return Usuario.query.get(int(user_id))