from flask import Flask,render_template
# from flask import render_template (pode ser feito separado)

# Importa o request para capturar dados enviados pelo formulário
from flask import request

app=Flask(__name__)
@app.route("/")
def index():
    # Renderiza o arquivo index.html
    return render_template("index.html")

# Processamento dos dados
# Define a rota / dados que aceita o método post
@app.route("/dados", methods=["POST"])
def dados():
    # Captura o valor enviado pelo campo "nome"
    nome= request.form.get("nome")
    # Captura o valor enviado pelo campo "idade"
    idade= request.form.get("idade")    
    # Envia os dados para o template dados.html
    return render_template("dados.html",nome=nome,idade=idade)
    
if __name__=="__main__":
    app.run(debug=True)