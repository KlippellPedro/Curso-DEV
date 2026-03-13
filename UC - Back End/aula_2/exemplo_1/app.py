from flask import Flask, render_template
# Cria a palicação Flask
app = Flask(__name__)
#Define a rota principal
@app.route("/")
def home():
    # Variaveis Python
    nome= "Valdisney"
    idade= "22"
    endereco= "Venâncio Aires 93"
    bairro= "CB"

    # Envia as variaveis para o html
    return render_template(
        "index.html",
        nome=nome,
        idade=idade,
        endereco=endereco,
        bairro=bairro
    )
# Executa o servidor
if __name__=="__main__":
    app.run(debug=True)