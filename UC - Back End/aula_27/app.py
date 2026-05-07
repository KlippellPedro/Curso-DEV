from flask import Flask, redirect, url_for, session
from config import SECRET_KEY
from database import init_db
from routes.auth_routes import main as auth
from routes.user_routes import main as user

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
init_db()
app.register_blueprint(auth)
app.register_blueprint(user)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('user.perfil'))
    return redirect(url_for('auth.login'))

if __name__ == "__main__":
    app.run(debug=True)