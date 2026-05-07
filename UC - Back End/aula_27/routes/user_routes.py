from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from models.user_model import get_user_by_id, update_user

main= Blueprint('user', __name__)

@main.route('/perfil', methods=['GET', 'POST'])
def perfil():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        update_user(session['user_id'],nome,email)
        flash('Perfil atualizado com sucesso!', 'success')
        return redirect(url_for('user.perfil'))
    
    user= get_user_by_id(session['user_id'])
    return render_template('perfil.html', user=user)

        