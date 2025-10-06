from flask import render_template, url_for
from fakepinterest import app
from flask_login import login_required
from fakepinterest.forms import FormCriarConta, FormLogin

@app.route("/")
def homepage():
    formLogin = FormLogin()
    return render_template("index.html", form=formLogin)

@app.route("/criar_conta")
def criar_conta():
    formCriarConta = FormCriarConta()
    return render_template("criar_conta.html", form=formCriarConta)

@app.route("/perfil/<username>")
@login_required
def perfil(username):
    return render_template("perfil.html", username=username)