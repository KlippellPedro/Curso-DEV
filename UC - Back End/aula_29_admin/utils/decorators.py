from functools import wraps # permite criar decorators
from flask import session, redirect, url_for # controle de sessão
from models.user_model import get_user_by_id # buscar usuario

def login_required(f): # decorator que exige login
    @wraps(f) # mantem metadados da função original
    def decorated(*args, **kwargs): # função interna
        if 'user_id' not in session: # verifica se o usuário está logado
            return redirect(url_for('auth.login')) # redireciona para login
        return f(*args, **kwargs) # executa a função original
    return decorated # retorna decorator

def admin_required(f): # decorator que exige admin
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        user = get_user_by_id(session['user_id']) # busca usuario logado

        if not user['is_admin']: # verifica se é admin
            return "Acesso negado" # bloqueia o acesso
        return f(*args, **kwargs) # permite execução
    return decorated
