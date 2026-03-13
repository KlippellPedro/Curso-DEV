'''
Sistema de uma calculadora básica, utilizando a função match case
'''
class Calculadora:
    def __init__(self,n1,n2,operacao):
        self.n1=n1
        self.n2=n2
        self.operacao=operacao
        self.resultado=None

    def calcular(self):
        match self.operacao:
            case "+":
                self.resultado= self.n1+self.n2
            case "-":
                self.resultado= self.n1-self.n2
            case "*":
                self.resultado= self.n1*self.n2
            case "/":
                if self.n2!=0:
                    self.resultado=self.n1/self.n2
                else:
                    return "Erro: Divisão por zero"
            case __:
                return "Você escolheu uma opção matemática que não existe no sistema."
        return f"Resultado: {self.resultado}"