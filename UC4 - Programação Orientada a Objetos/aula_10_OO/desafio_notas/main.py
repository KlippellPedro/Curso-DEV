from aluno import Aluno
from media import Media
from situacao import Situacao
def main():
    continuar= "SIM"
    while continuar== "SIM":
        print("-- Sistema de Notas --\n")
        nome= input("Nome do aluno: ")
        turma= input("Turma do aluno: ")
        n1= int(input("Primeira nota: "))
        n2= int(input("Segunda nota: "))
        n3= int(input("Terceira nota: "))
        n4= int(input("Quarta nota: "))
        n5= int(input("Quinta nota: "))

        aluno= Aluno(nome,turma,n1,n2,n3,n4,n5)
        media= Media(n1,n2,n3,n4,n5)
        media_final= media.calcular_media()
        situacao_final= Situacao.calcular_situacao(media_final)

        print("\n","-"*30,"\n")
        aluno.exibir_dados()
        print(f"Media final: {media_final:.1f}")
        print(f"Situação curricular: {situacao_final}")
        while True:
            novo= input("\nDeseja registrar um novo aluno: ").upper()
            if novo== "SIM":
                break
            elif novo== "NÃO":
                continuar= "NÃO"
                break
            else: 
                print("\nDIgite uma opção válida!")
                
if __name__ == "__main__":
    main()