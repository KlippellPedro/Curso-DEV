from flask import Flask, render_template, request
from controllers.contato_controller import ContatoController
from models.contato import Contato
from database.conexao import BancoDados

app = Flask(__name__)

# Cria o banco e a tabela automaticamente ao iniciar o sistema
BancoDados.criar_tabela()

# Rotas
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/oprograma")
def oprograma():
    return render_template("pages/oprograma.html")

@app.route("/consulta")
def consulta():
    return render_template("pages/consulta.html")

@app.route("/perguntas")
def perguntas():
    return render_template("pages/perguntas.html")

@app.route("/inscrever")
def inscrever():
    return render_template("pages/inscrever.html")

@app.route("/fale_conosco", methods=["GET","POST"])
def fale_conosco():
        
        if request.method == "POST":
        
            contato = Contato()
            contato.set_nome(request.form.get("nome"))
            contato.set_sobrenome(request.form.get("snome"))
            contato.set_datanasc(request.form.get("datanasc"))
            contato.set_endereco(request.form.get("endereco"))
            contato.set_bairro(request.form.get("bairro"))
            contato.set_cidade(request.form.get("cidade"))
            contato.set_estado(request.form.get("estado"))
            contato.set_sexo(request.form.get("sexo"))
            contato.set_telefone(request.form.get("telefone"))
            contato.set_email(request.form.get("email"))
            contato.set_usuario(request.form.get("usuario"))
            contato.set_senha(request.form.get("senha"))
            contato.set_observacao(request.form.get("obs"))

            controller = ContatoController()
            controller.salvar(contato)

            return """
            <script>
            alert("Cadastro realizado com sucesso!");
            window.location.href="/";
            </script>
            """

        return render_template("pages/fale_conosco.html")


if __name__ == "__main__":
     app.run(debug=True)