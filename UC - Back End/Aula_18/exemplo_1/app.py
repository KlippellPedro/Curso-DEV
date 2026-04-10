from flask import Flask, render_template, request
# Importa função que inicializa o banco
from database import init_db
# Importa função que cria conexão com o banco
from database import get_connection
# Importa a classe Contato
from models.contato import Contato

app = Flask(__name__)
# Inicializa o banco e cria a tabela se não existir
init_db()

# Rota principal
@app.route("/")
def index():
    return render_template("index.html")

# Rota para cadastrar contato
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    # Captura os dados enviados pelo formulário
    nome = request.form["nome"]
    email = request.form["email"]
    telefone = request.form["fone"]
    data_nascimento = request.form["data"]

    # Cria um objeto da classe Contato
    contato = Contato(nome, email, telefone, data_nascimento)
    # Salva o contato no banco
    contato.salvar()
    # Retorna para página com mensagem de sucesso
    return render_template("sucesso.html")

# Rota para listar contatos
@app.route("/listar")
def listar():
    # Cria conexão com o banco
    conn = get_connection()
    # Cria cursor para executar os comandos SQL
    cursor = conn.cursor()
    # Executa o comando SQL para buscar todos os registros
    cursor.execute("SELECT * FROM contato")
    # Guarda os registros encontrados
    contatos = cursor.fetchall()
    # Fecha conexão com o banco
    conn.close()
    # Envia lista de contatos para o template listar.html
    return render_template("listar.html", contatos=contatos)

if __name__ == "__main__":
    app.run(debug=True)