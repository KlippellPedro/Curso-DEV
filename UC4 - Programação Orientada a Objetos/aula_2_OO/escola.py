class Escola:
    def __init__(self):
        self.nome = "" 
        self.turma = "" 
        self.n1=0
        self.n2=0
        self.n3=0
        self.n4=0
        self.n5=0
        self.media=0.0
        
    def coletar_dados(self): 
        print("-- Sistema de Cadastro Escolar --")
        self.nome = input("Digite o nome do aluno: ")
        self.turma = input("Digite a turma do aluno: ")
        self.n1= int(input("Digite a primeira nota: "))
        self.n2= int(input("Digite a segunda nota: "))
        self.n3= int(input("Digite a terceira nota: "))
        self.n4= int(input("Digite a quarta nota: "))
        self.n5= int(input("Digite a quinta nota: "))
        self.media=(self.n1+self.n2+self.n3+self.n4+self.n5)/5

    def exibir_dados(self):
        print("")
        print(f"Nome: {self.nome}")
        print(f"Turma: {self.turma}")
        print(f"Primeira nota: {self.n1}")
        print(f"Segunda nota: {self.n2}")
        print(f"Terceira nota: {self.n3}")
        print(f"Quarta nota: {self.n4}")
        print(f"Quinta nota: {self.n5}")
        print(f"Média final: {self.media}")

if __name__ == "__main__":

    sistema = Escola()
    sistema.coletar_dados()
    sistema.exibir_dados()