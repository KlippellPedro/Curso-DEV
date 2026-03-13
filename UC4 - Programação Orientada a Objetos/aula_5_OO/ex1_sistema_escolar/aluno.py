class Aluno:
    '''
    Classe que representa um aluno e calcula sua media e situação curricular
    '''
    def __init__(self,nome,turma,notas):
        self.nome = nome
        self.turma = turma
        self.notas = notas
    def calcular_media(self):
        return sum(self.notas)/len(self.notas)
    def verificar_situacao(self):
        media=self.calcular_media()
        if media>=7:
            return "Aprovado"
        elif media>=5:
            return "Recuperação"
        else:
            return "Reprovado"