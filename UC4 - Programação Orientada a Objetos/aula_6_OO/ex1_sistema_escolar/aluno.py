class Aluno:
    '''
    Classe que representa um aluno com as suas notas.
    Calcular a média e a situação curricular
    '''
    def __init__(self,nome,turma,n1,n2,n3,n4,n5):
        self.nome= nome
        self.turma= turma
        self.n1= n1
        self.n2= n2
        self.n3= n3
        self.n4= n4
        self.n5= n5

    def calcular_media(self):
        '''
        Método para calcular as 5 notas e a média delas
        '''
        return (self.n1+self.n2+self.n3+self.n4+self.n5)/5
    
    def situacao_curricular(self):
        '''
        Método que verifica a situação curricular do aluno
        '''
        media= self.calcular_media()
        if media>=7:
            return "Aprovado"
        elif media>=5:
            return "Recuperação"
        else:
            return "Reprovado"
    