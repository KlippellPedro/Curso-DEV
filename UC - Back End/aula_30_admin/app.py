from flask import Flask, redirect, url_for, session
from database import init_db
from routes.auth_routes import bp as auth_bp
from routes.user_routes import bp as user_bp
from routes.admin_routes import bp as admin_bp
from models.user_model import get_user_by_id
from config import SECRET_KEY

app=Flask(__name__)
app.secret_key =SECRET_KEY

init_db()

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

@app.route('/')
def index():
    if 'user_id' in session:
        user = get_user_by_id(session['user_id'])
        
        if user['is_admin']:
            return redirect(url_for('admin.admin'))
        return redirect(url_for('user.perfil'))
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)