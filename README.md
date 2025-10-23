# 📌 FakePinterest

Projeto de rede social inspirada no Pinterest, desenvolvido em Python com Flask.

## 📚 Sobre o Projeto

Este projeto foi desenvolvido seguindo o minicurso **"Criação de Sites com Python"** da Hashtag Treinamentos.

🎥 **Link do curso:** [https://blp.hashtagtreinamentos.com/python/minicurso/criacao-sites-python](https://blp.hashtagtreinamentos.com/python/minicurso/criacao-sites-python)

## 🚀 Tecnologias Utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **Flask-Login** - Gerenciamento de autenticação
- **Flask-Bcrypt** - Criptografia de senhas
- **Flask-WTF** - Formulários web
- **SQLite** - Banco de dados

## 📋 Funcionalidades

- ✅ Cadastro de usuários
- ✅ Login/Logout
- ✅ Autenticação segura com hash de senha
- ✅ Upload de fotos
- ✅ Perfil de usuário
- ✅ Validação de formulários

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone <seu-repositorio>
cd fakepinterest
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
- **Windows:**
```bash
venv\Scripts\activate
```
- **Linux/Mac:**
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install flask flask-sqlalchemy flask-login flask-bcrypt flask-wtf
```

## 💻 Como Executar

1. Execute o aplicativo:
```bash
python main.py
```

2. Acesse no navegador:
```
http://127.0.0.1:5000
```

## 📁 Estrutura do Projeto

```
fakepinterest/
├── fakepinterest/
│   ├── __init__.py          # Configuração do Flask
│   ├── models.py            # Modelos do banco de dados
│   ├── routes.py            # Rotas da aplicação
│   ├── forms.py             # Formulários WTForms
│   ├── templates/           # Templates HTML
│   └── static/              # Arquivos estáticos (CSS, JS, imagens)
├── fakepinterest.db         # Banco de dados SQLite
└── main.py                  # Arquivo principal
```

## 🗄️ Modelos de Dados

### Usuario
- `id` - Identificador único
- `username` - Nome de usuário
- `email` - Email (único)
- `password` - Senha criptografada
- `fotos` - Relação com fotos postadas

### Foto
- `id` - Identificador único
- `image_url` - URL da imagem
- `data_postagem` - Data de upload
- `id_usuario` - Chave estrangeira para Usuario

## 🔐 Segurança

- Senhas são criptografadas usando **Bcrypt**
- Proteção CSRF nos formulários com **Flask-WTF**
- Validação de email e campos obrigatórios
- Rotas protegidas com `@login_required`

## 📝 Créditos

Projeto desenvolvido durante o minicurso da **Hashtag Treinamentos**.

## 📄 Licença

Este projeto é destinado para fins educacionais.

---

⭐ Desenvolvido com Python e Flask
