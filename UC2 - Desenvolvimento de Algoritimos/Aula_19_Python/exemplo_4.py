def media(nota1, nota2, nota3, nota4):
    resultado = (nota1+nota2+nota3+nota4)/4
    return resultado

def situacao(curriculo_media):
    if curriculo_media >= 7:
        return "Aprovado"
    elif curriculo_media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
def main():
    print("-- Sistema de notas e situação curricular --")
    nome = input("Digite o nome do aluno: ")
    turma = input("Digite a turma do aluno: ")
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    resultado = media(n1,n2,n3,n4)
    print("")
    print(f"Nome do aluno: {nome}")
    print(f"Turma: {turma}")
    print(f"Média final: {resultado:.2f}")
    situacao_curricular = situacao(resultado)
    print(f"Situação curricular: {situacao_curricular}")

if __name__ == "__main__":
    main()