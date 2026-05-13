from flask import Blueprint, render_template, request, session
from models.user_model import get_user_by_id, update_user
from utils.decorators import login_required

bp = Blueprint('user', __name__)

@bp.route('/perfil', methods=['GET', 'POST'])
@login_required # exige login
def perfil():
    user_id = session['user_id'] # pega id logado

    if request.method == 'POST':
        update_user(
            user_id,
            request.form.get('nome'),
            request.form.get('email')
        )

    user = get_user_by_id(user_id) # busca usuário
    return render_template('perfil.html', user=user)    