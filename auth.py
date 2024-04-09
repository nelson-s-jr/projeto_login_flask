from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required
from .models import User


auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password_check = request.form.get('password-check')

    user = User.query.filter_by(email=email).first()  # se isso retornar um usuário, o email ja existe no banco de dados

    if user:
        flash('Usuário já existente.')
        return redirect(url_for('auth.signup'))  # se o endpoint do parâmetro 
                                                 #   começa com '.', ele usará a rota do Blueprint
    elif password != password_check:
        flash('As senhas não conferem.')
        return redirect(url_for('auth.signup'))
    
    # criar um novo usuário com os dados do form. usar Hash nas senhas para que o texto não seja salvo
    new_user = User(email=email, name=name, 
                    password=generate_password_hash(password, method='pbkdf2:sha256'))

    # adicionando o usuário na base de dados
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/login')
def login():
    return render_template('login.html')



@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # checando se o usuário existe
    # pegue a senha de usuario, hash, e comparar com o hash da senha no banco de dados

    if password:
        check_password = check_password_hash(user.password, password)

    if not user or not check_password:
        flash('Usuário Inexistente ou Senha incorreta')
        return redirect(url_for('auth.login_post')) # Se o user nao existir ou a senha estiver incorreta, recarregue a pagina

    # se o check acima passar, o usuário tem as credenciais corretas
    login_user(user, remember=remember)
    return redirect(url_for('main.profile'))


@auth.route('/cadastro')
def signup():
    return render_template('signup.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))