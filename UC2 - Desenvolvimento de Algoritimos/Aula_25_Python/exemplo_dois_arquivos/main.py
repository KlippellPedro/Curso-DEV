from notas import media, situacao
# Importando a função media() do arquivo notas.py
def main():
    print("--- Sistema Escolar ---")
    nome = input("Digite o nome do aluno: ")
    turma = input("Digite a turma: ")
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))
    n4 = int(input("Digite a quarta nota: "))

    resultado = media(n1,n2,n3,n4)

    print("")
    print(f"Nome do aluno: {nome}")
    print(f"Turma: {turma}")
    print(f"Média final: {resultado:.1f}")

    situacao_curricular = situacao(resultado)
    print(f"Situação curricular: {situacao_curricular}")

if __name__ == "__main__":
    main()