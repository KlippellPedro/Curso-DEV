from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular_juros", methods=["POST"])
def calcular_juros():
    prestacao=float(request.form.get("prestacao"))
    dia_atraso= int(request.form.get("dia_atraso"))
    
    juros=None
    taxa=None
    prestacao_juros=None
    
    if  1 <= dia_atraso <= 3:
        prestacao_juros=prestacao*0.05
        juros=5
        resultado= prestacao_juros+prestacao
        
    elif dia_atraso<=9:
        prestacao_juros=prestacao*0.10
        juros=10
        resultado= prestacao_juros+prestacao
        
    elif dia_atraso>= 10:
        prestacao_juros=prestacao*0.15
        juros=15
        resultado= prestacao_juros+prestacao
        
    return render_template("resultado.html", prestacao=prestacao,dia_atraso=dia_atraso,juros=juros,taxa=taxa,prestacao_juros=prestacao_juros,resultado=resultado)

if __name__=="__main__":
    app.run(debug=True)