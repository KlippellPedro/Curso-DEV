# Sistema para realizar calculos
class Calcular:
    '''
    Classe responsável por realizar operações matemáticas
    basicas entre dois numeros
    '''
    def __init__(self):
        '''
        Método contrutor da classe calcular.
        inicializa os atributos v1 e v2 como 0
        self faz referência ao próprio objeto.
        '''
        self.v1 = 0
        self.v2 = 0
    
    def coletar_dados(self):
        '''
        Método que solicita ao usuário dois números inteiros
        '''
        print("-- Sistema de operações matemáticas basicas TabajaraCorp --")
        # Entrada dos valores, convertendo para inteiro
        self.v1 = int(input("Informe o primeiro número: "))
        self.v2 = int(input("Informe o segundo número: "))

    def somar(self):
        '''
        Método para realizar a soma dos dois valores.
        Retorna o resultado da soma.
        '''
        return self.v1 + self.v2
    
    def subtrair(self):
        '''
        Método para realizar a subtração dos dois valores.
        Retorna o resultado da subtração.
        '''
        return self.v1 - self.v2
    
    def multiplicar(self):
        '''
        Método para realizar a multiplicação dos dois valores.
        Retorna o resultado da multiplicação.
        '''
        return self.v1 * self.v2
    
    def dividir(self):
        '''
        Método para realizar a divisão dos dois valores.
        Retorna o resultado da  divisão.
        '''
        if self.v2 == 0:
            return "ERRO: Divisão por zero não é permitida."
        return self.v1 /self.v2
    
    def potencia(self):
        '''
        Método para realizar a potência do primeirovalor, elevado
        ao segundo valor.
        '''
        return self.v1 ** self.v2
    
    def exibir_resultados(self):
        '''
        Método para exibir resultados de todas as operações realizadas.
        '''
        print("\n","-"*40,"\n")
        print("Resultado da soma entre os dois valores")
        soma = self.somar()
        print(f"Resultado da soma: {soma}")
        print("\n","-"*40,"\n")
        print("Resultado da subtração entre os dois valores")
        subtracao = self.subtrair()
        print(f"Resultado da subtração: {subtracao}")
        print("\n","-"*40,"\n")
        print("Resultado da multiplicação entre os dois valores")
        multiplicacao = self.multiplicar()
        print(f"Resultado da multiplicação: {multiplicacao}")
        print("\n","-"*40,"\n")
        print("Resultado da divisão entre os dois valores")
        divisao = self.dividir()
        if isinstance(divisao, str): # Verifica se é uma mensagem de erro
            print(divisao)
        else:
            print(f"Resultado da divisão: {divisao}")
        print("\n","-"*40,"\n")
        print("Resultado da potencia entre os dois valores")
        potencia = self.potencia()
        print(f"Resultado da potencia: {potencia}")

# Bloco principal do sistema
if __name__ == "__main__":
    # Criando objeto da classe Calcular
    calc = Calcular()
    # Chamando o método para colear os dados
    calc.coletar_dados()
    # Chamando o método para exibir os resultados das operações
    calc.exibir_resultados()
