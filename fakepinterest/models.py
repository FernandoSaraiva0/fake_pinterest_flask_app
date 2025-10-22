# Creating database tables
from fakepinterest import database, loginManager
from datetime import datetime
from flask_login import UserMixin

#Function to load user for login management
@loginManager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(database.Model, UserMixin):
    id=database.Column(database.Integer, primary_key=True)
    username=database.Column(database.String(20), nullable=False)
    email=database.Column(database.String(120), nullable=False, unique=True)
    password=database.Column(database.String(60), nullable=False)
    fotos=database.relationship('Foto', backref='usuario', lazy=True)

class Foto (database.Model):
    id=database.Column(database.Integer, primary_key=True)
    image_url=database.Column(database.String, default='https://via.placeholder.com/150')
    # Timestamp of the post, with default value as current timestamp because utcnow() is not working
    data_postagem=database.Column(database.DateTime, nullable=False, default=database.func.current_timestamp())
    # Make a foreign key relationship with Usuario table
    id_usuario=database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False) 