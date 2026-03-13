from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    # Verificando as variáveis
    i=1 # define a variável como inteira
    b_integer=isinstance(i,int) #Verifica se é do tipo inteiro
    
    s="Minha String" # Define a variavel como string
    b_string = isinstance(s,str) # Verifica se é do tipo string
    
    f=1.9 # define a variavel como float
    b_float=isinstance(f,float) # verifica se é do tipo float
    
    t=True # define a variavel como booleano
    b_bool= isinstance(t,bool) # verifica se é do tipo booleana
    
    a= [] # define a variavel como array (lista)
    b_array= isinstance(a,list) # verifica se é do tipo array
    
    v= 1
    b_isset= v is not None # verifica se não é None (verifica se "v" esta recebendo as informações)
    
    return render_template(
        "index.html",
        b_integer=b_integer,
        b_string=b_string,
        b_float=b_float,
        b_bool=b_bool,
        b_array=b_array,
        b_isset=b_isset
    )
if __name__=="__main__":
    app.run(debug=True)
    