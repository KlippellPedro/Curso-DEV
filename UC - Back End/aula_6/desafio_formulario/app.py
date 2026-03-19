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
# Define a rota / dados (GET é padrão no Flask)
@app.route("/meusdados")
def dados():
    nome= request.args.get("nome")
    data_nasc= request.args.get("data_nasc")
    idade= request.args.get("idade")
    endereco= request.args.get("endereco")
    bairro= request.args.get("bairro")
    cidade= request.args.get("cidade")
    estado= request.args.get("estado")
    celular= request.args.get("celular")
    email= request.args.get("email")
    cpf= request.args.get("cpf")
    rg= request.args.get("rg")
    
    
    # Verificar se os dados foram enviados
    if nome and data_nasc and idade and endereco and bairro and cidade and estado and celular and email and cpf and rg:
        mensagem= "Aqui estão seus dados!"
    else:
        mensagem= "Nenhum dado foi enviado."
        
    # Envia os dados para o template dados.html
    return render_template("meusdados.html",nome=nome,data_nasc=data_nasc,idade=idade,endereco=endereco,bairro=bairro,cidade=cidade,estado=estado,celular=celular,email=email,cpf=cpf,rg=rg,mensagem=mensagem)
    
if __name__=="__main__":
    app.run(debug=True)