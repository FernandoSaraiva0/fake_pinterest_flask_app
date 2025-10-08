from flask import render_template, url_for, redirect
from fakepinterest import app, database, bcrypt
from flask_login import login_required
from fakepinterest.forms import FormCriarConta, FormLogin
from fakepinterest.models import Usuario, Foto

@app.route("/", methods=['GET', 'POST'])
def homepage():
    formLogin = FormLogin()
    return render_template("index.html", form=formLogin)

@app.route("/criar_conta", methods=['GET', 'POST'])
def criar_conta():
    formCriarConta = FormCriarConta()
    if formCriarConta.validate_on_submit():
        usuario = Usuario(
            email=formCriarConta.EmailField.data,
            username=formCriarConta.UsernameField.data,
            password=bcrypt.generate_password_hash(formCriarConta.PasswordField.data)
        )
        database.session.add(usuario)
        database.session.commit()
        return redirect(url_for('perfil', username=usuario.username))
    return render_template("criar_conta.html", form=formCriarConta)

@app.route("/perfil/<username>")
@login_required
def perfil(username):
    return render_template("perfil.html", username=username)