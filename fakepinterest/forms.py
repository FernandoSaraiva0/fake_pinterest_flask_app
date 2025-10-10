from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from fakepinterest.models import Usuario
class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    botao= SubmitField('Entrar')

class FormCriarConta(FlaskForm):
    EmailField = StringField('Email', validators=[DataRequired(), Email()])
    UsernameField = StringField('Nome de Usuário', validators=[DataRequired(), Length(min=3, max=25)])
    PasswordField1 = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    PasswordField2 = PasswordField('Confirme a Senha', validators=[DataRequired(), Length(min=6), EqualTo('PasswordField1', message='As senhas devem coincidir.')])
    SubmitField = SubmitField('Criar Conta')

    def validate_email(self, EmailField):
        # Aqui você pode adicionar a lógica para verificar se o nome de usuário já existe no banco de dados
        usuario = Usuario.query.filter_by(email=EmailField.data).first()
        if usuario:
            raise ValidationError('Este email já está em uso. Por favor, escolha outro.')       