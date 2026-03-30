from flask import Flask, render_template, request
app = Flask(__name__)

# Criando a classe
class Aluno:
    # Método construtor da classe
    def __init__(self):
        # Atributos privados
        self._nome = None
        self._idade = None
        self._cpf = None
        self._email = None
        self._telefone = None
        self._endereco = None
        self._cidade = None
        self._estado = None

    # Método GET para retornar valores
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return self._idade
    
    def get_cpf(self):
        return self._cpf
    
    def get_email(self):
        return self._email
    
    def get_telefone(self):
        return self._telefone
    
    def get_endereco(self):
        return self._endereco
    
    def get_cidade(self):
        return self._cidade
    
    def get_estado(self):
        return self._estado
    
    # Método SET alteram os valores
    def set_nome(self, nome):
        self._nome = nome

    def set_idade(self, idade):
        self._idade = idade

    def set_cpf(self, cpf):
        self._cpf = cpf

    def set_email(self, email):
        self._email = email

    def set_telefone(self, telefone):
        self._telefone = telefone

    def set_endereco(self, endereco):
        self._endereco = endereco

    def set_cidade(self, cidade):
        self._cidade = cidade

    def set_estado(self, estado):
        self._estado = estado                        

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Rota de processamento dos dados
@app.route("/dados", methods=["POST"])
def dados():
    # Recebe os dados enviados pelo formulário
    nome = request.form["nome"]
    idade = request.form["idade"]
    cpf = request.form["cpf"]
    email = request.form["email"]
    telefone = request.form["telefone"]
    endereco = request.form["endereco"]
    cidade = request.form["cidade"]
    estado = request.form["estado"]

    # Cria uma instância do objeto da classe Aluno
    aluno = Aluno()
    # Usa o método SET para inserir os dados
    aluno.set_nome(nome)
    aluno.set_idade(idade)
    aluno.set_cpf(cpf)
    aluno.set_email(email)
    aluno.set_telefone(telefone)
    aluno.set_endereco(endereco)
    aluno.set_cidade(cidade)
    aluno.set_estado(estado)

    return render_template(
        "resultado.html",
        nome=aluno.get_nome(),
        idade=aluno.get_idade(),
        cpf=aluno.get_cpf(),
        email=aluno.get_email(),
        telefone=aluno.get_telefone(),
        endereco=aluno.get_endereco(),
        cidade=aluno.get_cidade(),
        estado=aluno.get_estado()
    )
if __name__ == "__main__":
    app.run(debug=True)

