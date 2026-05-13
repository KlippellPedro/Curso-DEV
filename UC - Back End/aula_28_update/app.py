from flask import Flask, redirect, url_for, session
from config import SECRET_KEY
from database import init_db
from routes.auth_routes import bp as auth_bp
from routes.user_routes import bp as user_bp

app = Flask(__name__)
app.secret_key = SECRET_KEY

init_db()

app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('user.perfil'))
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)