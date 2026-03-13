from flask import Flask, render_template
app= Flask(__name__)
@app.route("/")
def index():
    # Trabalhando com funções

    # Define uma função que retorna um mensagem
    def msg():
        return "Hello World!"
    
    # Chama a função 
    mensagem= msg()

    # Função que recebe um nome
    def nomeAluno(aluno):
        return aluno
    
    # Lista de alunos (chamada pela função)
    alunos= [
        nomeAluno("Pedro"),
        nomeAluno("Vinicius"),
        nomeAluno("Gabriel"),
        nomeAluno("Camille"),
        nomeAluno("Giovanna")
    ]

    # Função que recebe dois argumentos, nome e idade
    def nomeIdade(nome, idade):
        return f"Seu nome é: {nome}, e sua idade é: {idade}"
    # Lista com o nome e idade
    pessoas = [
        nomeIdade("Pedro", 19),
        nomeIdade("Vinicius", 19),
        nomeIdade("Gabriel", 20),
        nomeIdade("Camille", 21),
        nomeIdade("Giovanna", 19)
    ]
    # Declaração de variável do tipo global (faz a variavel ser de acesso global)
    global b
    # Função pra somar
    def soma(a):
        global b
        b=a+5

    # Chama a função
    soma(10)

    valor_b = b

    # Outro exemplo de variável global
    global a
    a=1
    b=2

    def calcula():
        global a,b
        b=a +b

    calcula()
    resultado_calculo = b

    # Envia todos os dados para o HTML
    return render_template(
        "index.html",
        mensagem=mensagem,
        alunos=alunos,
        pessoas=pessoas,
        valor_b=valor_b,
        resultado_calculo=resultado_calculo
    )

if __name__ == "__main__":
    app.run(debug=True)