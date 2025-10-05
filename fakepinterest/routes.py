from flask import render_template, url_for
from fakepinterest import app

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/perfil/<username>")
def perfil(username):
    return render_template("perfil.html", username=username)