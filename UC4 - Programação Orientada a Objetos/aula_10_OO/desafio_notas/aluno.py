class Aluno:
    def __init__(self,nome,turma,n1,n2,n3,n4,n5):
        self.nome=nome
        self.turma=turma
        self.n1=n1
        self.n2=n2
        self.n3=n3
        self.n4=n4
        self.n5=n5

    def exibir_dados(self):
        print(f"Nome Aluno: {self.nome}")
        print(f"Turma: {self.turma}")
        print(f"Primeira nota: {self.n1}")
        print(f"Segunda nota: {self.n2}")
        print(f"Terceira nota: {self.n3}")
        print(f"Quarta nota: {self.n4}")
        print(f"Quinta nota: {self.n5}")