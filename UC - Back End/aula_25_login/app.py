from flask import Flask, render_template, request, redirect, url_for,session
from controllers.usuario_controller import UsuarioController
from database.conexao import Conexao

app = Flask(__name__)
app.SECRET_KEY = 'chave_super_secreta'
Conexao.criar_tabela()

# Rota principal
@app.route("/")
def index():
    if "usuario" in session:
        return redirect(url_for("home"))
    return render_template("login.html")

# Rota para cadastrar usuário
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome")
    email = request.form.get("email")
    senha = request.form.get("senha")

    controller = UsuarioController()
    controller.cadastrar(nome, email, senha)

    return """
    <script>
    alert("Usuário cadastrado com sucesso!");
    window.location.href="/";
    </script>
    """
# Rota para o login
@app.route("/logar", methods=["POST"])
def logar():
    email = request.form.get("email")
    senha = request.form.get("senha")

    controller = UsuarioController()
    usuario=controller.login(email, senha)
    
    if usuario:
        session["usuario"] = usuario["nome"]
        return redirect(url_for("home"))
    else:
        return """
        <script>
        alert("E-mail ou senha inválidos!");
        window.location.href="/";
        </script>
        """
    
@app.route("/home")
def home():
    if "usuario" not in session:
        return redirect(url_for("index"))
    return render_template("home.html", nome=session["usuario"])

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("index"))
    
if __name__ == "__main__":
    app.run(debug=True)