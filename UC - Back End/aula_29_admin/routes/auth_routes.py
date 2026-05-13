from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import create_user, get_user_by_email
import sqlite3

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        if not nome or not email or not senha: # Valida campos
            flash('Preencha todos os campos')
            return redirect(url_for('auth.register'))
        try:
            create_user(nome,email,generate_password_hash(senha))
            flash('Cadastro realizado!')
            return redirect(url_for('auth.login'))
        except sqlite3.IntegrityError: # erro e-mail duplicado
            flash('E-mail já existe')

    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        user = get_user_by_email(email)

        if user and check_password_hash(user['senha'], senha): # valida a senha
            session['user_id'] = user['id'] # salva o id na sessão

            # Verifica se é admin
            if user['is_admin']: # se for admin
                return redirect(url_for('admin.admin')) # vai direto para o painel admin
            return redirect(url_for('user.perfil')) # senão vai para perfil
        flash('Login inválido!')

    return render_template('Login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))    

                
