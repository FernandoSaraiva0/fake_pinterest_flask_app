# Creating database tables
from fakepinterest import database, loginManager
from datetime import datetime
from flask_login import UserMixin

def load_user(user_id):
    return Usuario.query.get(int(user_id))

class Usuario(database.Model, UserMixin):
    id=database.Column(database.Integer, primary_key=True)
    username=database.Column(database.String(20), nullable=False)
    email=database.Column(database.String(120), nullable=False, unique=True)
    senha=database.Column(database.String(60), nullable=False)
    fotos=database.relationship('Foto', backref='username', lazy=True)

class Foto (database.Model):
    id=database.Column(database.Integer, primary_key=True)
    image_url=database.Column(database.String, default='https://via.placeholder.com/150')
    # Timestamp of the post, with default value as current timestamp because utcnow() is not working
    data_postagem=database.Column(database.DateTime, nullable=False, default=database.func.current_timestamp())
    # Make a foreign key relationship with Usuario table
    id_usuario=database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False) 