from flask import Flask, render_template, request
from database import init_db
from database import get_connection
from registro import Registro

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    sobrenome = request.form["sobrenome"]
    endereco=request.form["endereco"]
    numero=request.form["numero"]
    comple=request.form["comple"]
    bairro=request.form["bairro"]
    cidade=request.form["cidade"]
    estado=request.form["estado"]
    data_nasc = request.form["data_nasc"]
    cpf=request.form["cpf"]
    rg=request.form["rg"]
    telefone=request.form["telefone"]
    email=request.form["email"]

    cliente = Registro(nome,sobrenome,endereco,numero,comple,bairro,cidade,estado,data_nasc,cpf,rg,telefone,email)
    cliente.salvar()
    return render_template("sucesso.html")

# Rota para listar contatos
@app.route("/listar")
def listar():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    # Envia lista de contatos para o template listar.html
    return render_template("listar.html", clientes=clientes)

if __name__ == "__main__":
    app.run(debug=True)