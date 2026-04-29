from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app=Flask(__name__)
# Caminho do banco
DATABASE= "databese.db"

def connect_database():
    conn=sqlite3.connect(DATABASE)
    conn.row_factory=sqlite3.Row # permite acessar colunas pelo nome
    return conn

# Função para criar banco e tabela
def create_database():
    conn=connect_database()
    cursor=conn.cursor()
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS fale_conosco(
        id INTEGER PRIMARY_KEY AUTOINCREMET,
        nome TEXT,
        sobrenome TEXT,
        data_nasc TEXT,
        endereco TEXT,
        bairro TEXT,
        cidade TEXT,
        estado TEXT,
        sexo TEXT,
        telefone TEXT,
        email TEXT,
        usuario TEXT,
        senha TEXT,
        observacao TEXT
    )""")
    conn.commit()
    conn.close()
    
# Cria o banco ao iniciar o sistema
create_database()

@app.route("/")
def index():
    return render_template("index.html")

# Rota para página oprograma
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

@app.route("/fale_conosco", methods=["GET", "POST"])
def fale_conosco():
    # Se o formulario foi enviado
    if request.method=="POST":
        nome=request.form.get("nome")
        sobrenome=request.form.get("sobrenome")
        data_nasc=request.form.get("data_nasc")
        endereco=request.form.get("endereco")
        bairro=request.form.get("bairro")
        cidade=request.form.get("cidade")
        estado=request.form.get("estado")
        sexo=request.form.get("sexo")
        telefone=request.form.get("telefone")
        email=request.form.get("email")
        usuario=request.form.get("usuario")
        senha=request.form.get("senha")
        observacao=request.form.get("observacao")

        conn=connect_database()
        cursor=conn.cursor()
        
        cursor.execute("""INSERT INTO fale_conosco (nome,sobrenome,data_nasc,endereco,bairro,cidade,estado,sexo,telefone,email,usuario,senha,observacao) 
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",(nome,sobrenome,data_nasc,endereco,bairro,cidade,estado,sexo,telefone,email,usuario,senha,observacao))
        conn.commit()
        conn.close()
        
        # Redireciona para pagina inicial após salvar
        return """
        <script>
        alert("Cadastro realizado com sucesso!");
        window.location.href="/";
        </script>
        """
    return render_template("pages/fale_conosco.html")

# Rota listar dados do banco
@app.route("/listar")
def listar():
    conn=connect_database()
    cursor=conn.cursor()
    
    cursor.execute("SELECT * FROM fale_conosco")
    dados=cursor.fetchall()
    conn.close()
    
    return render_template("pages/consulta.html", dados=dados)

if __name__=="__main__":
    app.run(debug=True)