from flask import render_template, url_for, redirect, flash
from fakepinterest import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakepinterest.forms import FormCriarConta, FormLogin, FormPostPhoto
from fakepinterest.models import Usuario, Foto
import os
from werkzeug.utils import secure_filename # For handling file uploads

@app.route("/", methods=['GET', 'POST'])
def homepage():
    formLogin = FormLogin()
    
    if formLogin.validate_on_submit():
        usuario = Usuario.query.filter_by(
            email=formLogin.EmailField.data
            ).first()
        
        if usuario and bcrypt.check_password_hash(
            usuario.password, formLogin.PasswordField.data
            ):
            login_user(usuario)
            flash(f'Login realizado com sucesso! Bem-vindo(a) de volta, {usuario.username}!', 'success')
            return redirect(url_for('perfil', id_usuario=usuario.id))
        else:
            flash('Falha no login. Verifique seu email e senha.', 'danger') 

    return render_template("index.html", form=formLogin)

@app.route("/criar_conta", methods=['GET', 'POST'])
def criar_conta():
    formCriarConta = FormCriarConta()

    # DEBUG: Verificar se o formulário foi enviado
    if formCriarConta.is_submitted():
        print(f"Formulário enviado! Validação: {formCriarConta.validate()}")
        print(f"Erros: {formCriarConta.errors}")

    if formCriarConta.validate_on_submit():
        try:
            user_exists = Usuario.query.filter_by(
                email=formCriarConta.EmailField.data
                ).first()
            if user_exists:
                flash('Email já cadastrado. Por favor, utilize outro email.', 'danger')
                return redirect(url_for('criar_conta'))

            #Password hashing
            password_crypt = bcrypt.generate_password_hash(
                formCriarConta.PasswordField2.data
                ).decode('utf-8')
            
            #Create new user instance
            usuario = Usuario(
                email=formCriarConta.EmailField.data,
                username=formCriarConta.UsernameField.data,
                password=password_crypt
            )
            database.session.add(usuario)
            #Commit the new user to the database
            database.session.commit()
            
            # DEBUG: Log the username being registered
            print('Cadastrando o usuário:', usuario.username)
            #Login the user after account creation
            login_user(usuario, remember=True) ## Remember me is set to True by default here - armazena o login nos cookies
            flash(f'Conta criada com sucesso! Bem-vindo(a), {usuario.username}!', 'success')

            return redirect(url_for('perfil', usuario=usuario.id))
        
        except Exception as e:
            database.session.rollback()
            flash('Ocorreu um erro ao criar a conta. Por favor, tente novamente.', 'danger')
            print('Erro ao criar conta:', e)
            return render_template("criar_conta.html", form=formCriarConta)
    
    if formCriarConta.errors:
        print(f"Erros de validação: {formCriarConta.errors}")
        
    return render_template("criar_conta.html", form=formCriarConta)

@app.route("/perfil/<id_usuario>", methods=['GET', 'POST']) 
@login_required
def perfil(id_usuario):
    if int(id_usuario) == int(current_user.id): #Verifica se o usuário está acessando seu próprio perfil
        #Funcionalidade de postar foto
        form_foto = FormPostPhoto()
            # Handle photo posting
        if form_foto.validate_on_submit():
            nova_foto = form_foto.PhotoField.data
            secure_filename_nome = secure_filename(nova_foto.filename)
            caminho_salvar = os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], secure_filename_nome)
            nova_foto.save(caminho_salvar)
            # Create new Foto instance
            foto = Foto(
                image_url=secure_filename_nome,
                id_usuario=current_user.id
            )
            database.session.add(foto)
            database.session.commit()
            flash('Foto postada com sucesso!', 'success')
        return render_template("perfil.html", username=current_user.username, form=form_foto)
    else: #Acessando o perfil de outro usuário
        usuario = Usuario.query.get(int(id_usuario))
        return render_template("perfil.html", usuario=usuario, form=None) #Passa o objeto usuário para o template

# Logout route 
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Você saiu da sua conta com sucesso.', 'success')
    return redirect(url_for('homepage'))