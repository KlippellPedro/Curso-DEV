'''
Sistema para calcular o atraso de uma prestação
'''
class Sistemacobranca:
    '''
    Sistema para calcular o valor de uma prestação
    com juros de 2% de atraso por dia
    '''
    def __init__(self, valor_prestacao,dias_atraso,taxas_juros_diario = 0.02):
        '''
        Método contrutor que inicializa o sistema com o valor da 
        prestação, dias em atraso e taxa de juros diário
        '''
        self.valor_prestacao = valor_prestacao
        self.dias_atraso = dias_atraso
        self.taxas_juros_diario = taxas_juros_diario
    
    def calcular_total(self):
        '''
        Método para calcular o valor total da prestação com juros
        '''
        return self.valor_prestacao+(self.valor_prestacao*self.taxas_juros_diario*self.dias_atraso)
    
    def calcular_juros(self):
        '''
        Método para calcular o valor do juros cobrado.
        '''
        return self.calcular_total()-self.valor_prestacao
    
if __name__ == "__main__":
    print("-- Sistema de Cobraça TabajaraCorp --\n")
    valor = float(input("Digite o valor da prestação R$ "))
    atraso = int(input("Digite a quantos dias a prestação esta atrasada: "))

    # Criar uma instância da classe
    sistema = Sistemacobranca(valor,atraso)

    # Calcula os valores
    total= sistema.calcular_total()
    juros= sistema.calcular_juros()

    print("\n","-"*40,"\n")
    print(f"Valor da prestação R$ {valor:.2f}")
    print(f"Quantidade de dias em atraso: {atraso}")
    print(f"Valor do juros cobrado R$ {juros:.2f}")
    print(f"Valor total da prestação com juros R$ {total}")