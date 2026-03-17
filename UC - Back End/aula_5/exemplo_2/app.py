from flask import Flask, render_template
# Importa o datetime para trabalhar com data e hora
from datetime import datetime
# Importa o ZoneInfo para definir o horario
from zoneinfo import ZoneInfo
app = Flask(__name__)
@app.route("/")
def index():
    # Define o fuso horario de sp
    fuso = ZoneInfo("America/Sao_Paulo")
    # Obtém data e hora atual com fuso cofigurado
    agora= datetime.now(fuso)
    
    #weekday() retorna:
    # 0 = domingo / 6 = sabado
    wday = (agora.weekday() +1) % 7
    
    match wday:
        case 0:
            mensagem = "Domingo"
        case 1:
            mensagem= "Segunda"
        case 2:
            mensagem= "Terça"
        case 3:
            mensagem= "Quarta"
        case 5:
            mensagem= "Sexta"
        case 6:
            mensagem= "Sabado"
        case _:
            mensagem= "Quinta "
            
    return render_template(
        "index.html",
        mensagem=mensagem
    )        
    
if __name__=="__main__":
    app.run(debug=True)