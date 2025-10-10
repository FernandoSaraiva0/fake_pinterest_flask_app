from flask import render_template, url_for, redirect, flash
from fakepinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user
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
        password_crypt = bcrypt.generate_password_hash(formCriarConta.PasswordField1.data).decode('utf-8')

        usuario = Usuario(
            email=formCriarConta.EmailField.data,
            username=formCriarConta.UsernameField.data,
            password=password_crypt
        )
        database.session.add(usuario)
        database.session.commit()

        login_user(usuario, remember=True)
        flash(f'Conta criada com sucesso! Bem-vindo(a), {usuario.username}!', 'success')

        return redirect(url_for('perfil', usuario=usuario.username))
    return render_template("criar_conta.html", form=formCriarConta)

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)