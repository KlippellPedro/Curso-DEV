from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import create_user, get_user_by_email

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = generate_password_hash(request.form['senha'])

        try:
            create_user(nome, email, senha)
            flash('Cadastro realizado com sucesso!')
            return redirect(url_for('auth.login'))
        except:
            flash('E-mail já cadastrado!')

    return render_template('register.html') 

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        user = get_user_by_email(email)

        if user and check_password_hash(user['senha'], senha):
            session['user_id'] = user['id']
            return redirect(url_for('user.perfil'))
        else:
            flash('Credenciais inválidas!')

    return render_template('login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))               
