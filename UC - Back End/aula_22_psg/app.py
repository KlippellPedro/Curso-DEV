from flask import Flask, render_template, request, redirect, url_for
from controllers.aluno_controller import AlunoController
from database.conexao import Conexao

app = Flask(__name__)

# Chama o método para criar a tabela automaticamente se ela não existir
Conexao.criar_tabela()

@app.route("/")
def index():
    return render_template("index.html")

# Rota responsável por processar o cadastro do aluno
@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get("nome")
    sobrenome = request.form.get("sobrenome")
    idade = request.form.get("idade")

    controller = AlunoController()

    controller.salvar(nome, sobrenome, idade)

    # Exibe mensagem de sucesso
    return """
    <script>
    alert("Cadastro realizado com sucesso!");
    window.location.href = "/";
    </script>
    """

if __name__ == "__main__":
    app.run(debug=True)