class Calculadora:
    '''
    Classe que simula uma calculadora básica com operações de
    adição, subtração multiplicação e divisão
    '''
    def __init__(self,n1,n2,opcao):
        # Inicializa os números e a opção escolhida
        self.n1 = n1
        self.n2=n2
        self.opcao=opcao
        self.resultado= None

    def calcular(self):
        '''
        Método para realizar as operações matemáticas escolhidas
        '''
        if self.opcao=="+":
            self.resultado= self.n1+self.n2
        elif self.opcao=="-":
            self.resultado= self.n1-self.n2
        elif self.opcao=="*":
            self.resultado= self.n1*self.n2
        elif self.opcao=="/":
            if self.n2!=0:
                self.resultado= self.n1/self.n2
            else:
                self.resultado= None
        else:
            self.resultado=None
        
        return self.resultado