#Create a database sqlite with name defined in __init__.py
from fakepinterest import database, app

# Import models to register the tables
from fakepinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()