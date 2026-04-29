from flask import Flask,render_template,request
from controllers.contato_controller import ContatoController
from database.conexao import DataBase
from models.contato import Contato

app = Flask(__name__)

DataBase.create_table()

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/oprograma')
def oprograma():
    return render_template('pages/oprograma.html')
    
@app.route('/consulta')
def consulta():
    return render_template('pages/consulta.html')
    
@app.route('/perguntas')
def perguntas():
    return render_template('pages/perguntas.html')
    
@app.route('/inscrever')
def inscrever():
    return render_template('pages/inscrever.html')
    
@app.route('/fale_conosco', methods=['GET', 'POST'])
def fale_conosco():
    if request.method == 'POST':
        contato = Contato()
        contato.set_nome(request.form.get('nome'))
        contato.set_sobrenome(request.form.get('sobrenome'))
        contato.set_data_nascimento(request.form.get('data_nascimento'))
        contato.set_endereco(request.form.get('endereco'))
        contato.set_bairro(request.form.get('bairro'))
        contato.set_cidade(request.form.get('cidade'))
        contato.set_estado(request.form.get('estado'))
        contato.set_sexo(request.form.get('sexo'))
        contato.set_telefone(request.form.get('telefone'))
        contato.set_email(request.form.get('email'))
        contato.set_usuario(request.form.get('usuario'))
        contato.set_senha(request.form.get('senha'))
        contato.set_observacao(request.form.get('observacao'))
            
        controller = ContatoController()
        controller.salvar(contato)
        return """
        <script>
        alert("Cadastro realizado com sucesso!");
        window.location.href = "/";
        </script>
        """
    return render_template('pages/fale_conosco.html')

def listar():
    conn=DataBase.get_connection()
    cursor=conn.cursor()
    
    cursor.execute("SELECT * FROM fale_conosco")
    dados=cursor.fetchall()
    conn.close()
    
    return render_template("pages/consulta.html", dados=dados)

if __name__ == "__main__":
    app.run(debug=True)