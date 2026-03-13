from aluno import Aluno

def main():
    print("-- Sistema de Notas Klippel LTDA --")
    nome= input("Digite o nome do aluno: ")
    turma= str(input("Digite a turma: "))
    n1= int(input("Digite a primeira nota: "))
    n2= int(input("Digite a segunda nota: "))
    n3= int(input("Digite a terceira nota: "))
    n4= int(input("Digite a quarta nota: "))
    n5= int(input("Digite a quinta nota: "))

    # Criar um objeto aluno com os dados fornecidos
    aluno= Aluno(nome,turma,n1,n2,n3,n4,n5)

    media= aluno.calcular_media()
    situacao= aluno.situacao_curricular()

    print("")
    print(f"Nome do aluno: {aluno.nome}")
    print(f"Turma: {aluno.turma}")
    print(f"Primeira nota: {aluno.n1}")
    print(f"Segunda nota: {aluno.n2}")
    print(f"Terceira nota: {aluno.n3}")
    print(f"Quarta nota: {aluno.n4}")
    print(f"Quinta nota: {aluno.n5}")
    print(f"Média final: {media:.1f}")
    print(f"Situação curricular: {situacao}")

if __name__ == "__main__":
    main()