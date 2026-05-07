from flask import Flask,render_template,request,redirect,session
from controllers.usuario_controller import UsuarioController
from database.conexao import Conexao

app=Flask(__name__)
app.secret_key="segredo_super"
Conexao.criar_tabela()

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method=="POST":
        nome=request.form.get["nome"]
        email=request.form.get["email"]
        senha=request.form.get["senha"]
        
        controller=UsuarioController()
        erro=controller.validar(nome,email,senha)
        if erro:
            return f"<script>alert('{erro}');window.location.href='/cadastro';</script>"
        controller.cadastrar(nome,email,senha)
        return "<script>alert('Cadastro realizado!');window.location.href='/';</script>"
    return render_template("cadastro.html")

@app.route("/login", methods=["GET","POST"])
def login():
    email=request.form.get("email")
    senha=request.form.get("senha")
    controller=UsuarioController()
    usuario=controller.login(email,senha)
    if usuario:
        session["usuario"]=usuario["nome"]
        session["admin"]=usuario["admin"]
        return redirect("/home")
    return "<script>alert('Login invalido!');window.location.href='/';</script>"

@app.route("/home")
def home():
    if "usuario" not in session:
        return redirect("/")
    return render_template("home.html", nome=session["usuario"])

@app.route("/admin")
def admin():
    if "admin" not in session:
        return redirect("/")
    controller=UsuarioController()
    usuario=controller.listar()
    return render_template("admin.html",usuario=usuario)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/recuperar", methods=["GET","POST"])
def recuperar():
    if request.method=="POST":
        email=request.form.get("email")
        controller=UsuarioController()
        controller.gerar_token(email)
        return "<script>alert('E-mail enviado!');window.location.href='/';</script>"
    return render_template("recuperar.html")

@app.route("/redefinir/<token>", methods=["GET","POST"])
def redefinir(token):
    controller=UsuarioController()
    if not controller.validar_token(token):
        return "Token expirado ou invalido!"
    if request.method=="POST":
        senha=request.form.get("senha")
        return "<script>alert('Senha alterada!');window.location.href='/';</script>"
    return render_template("redefinir.html")

if __name__=="__main__":
    app.run(debug=True)