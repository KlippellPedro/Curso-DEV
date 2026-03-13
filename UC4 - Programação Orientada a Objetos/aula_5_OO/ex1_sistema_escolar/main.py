from aluno import Aluno

def main():
    print("-- Sistema Escolar Klippel LTDA --\n")
    nome= input("Digite o nome do aluno: ")
    turma= input("Digite a turma: ")
    n1= int(input("Digite a primeira nota: "))
    n2= int(input("Digite a segunda nota: "))
    n3= int(input("Digite a terceira nota: "))
    n4= int(input("Digite a quarta nota: "))
    n5= int(input("Digite a quinta nota: "))

    # Criando um vetor para armazenar as notas
    notas = [n1,n2,n3,n4,n5]

    # Criando uma instância com a classe Aluno, enviando os dados
    aluno= Aluno(nome,turma,notas)

    media= aluno.calcular_media()
    situacao= aluno.verificar_situacao()

    print("\n--- Dados do aluno ---\n")
    print(f"Nome do aluno: {aluno.nome}")
    print(f"Turma: {aluno.turma}")
    print(f"Nota 1: {n1}")
    print(f"Nota 2: {n2}")
    print(f"Nota 3: {n3}")
    print(f"Nota 4: {n4}")
    print(f"Nota 5: {n5}")
    print(f"Média final: {media:.2f}")
    print(f"Situação curricular: {situacao}")

if __name__ == "__main__":
    main()