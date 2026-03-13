class SistemaCobranca:
    '''
    Classe que representa um sistema de cobrança com juros sobre atraso na prestação
    '''
    def __init__(self, prestacao,dias_atraso, taxa_mensal):
        '''
        Inicializa os dados do sistema
        '''
        self.prestacao = prestacao
        self.dias_atraso = dias_atraso
        self.taxa_mensal = taxa_mensal
    def calcular_taxa_diaria(self):
        '''
        Método para converter a taxa n=mensal em taxa diaria
        '''
        return (self.taxa_mensal/100)/30
    def calcular_valor_juros(self):
        '''
        Calcula o valor total dos juros cobrados pelo atraso
        '''
        taxa_diaria= self.calcular_taxa_diaria()
        juros= self.prestacao *taxa_diaria* self.dias_atraso
        return juros
    def calcular_valor_total(self):
        '''
        Calcula o valor total a ser pago (prestacao+juros)
        '''
        return self.prestacao+self.calcular_valor_juros()

if __name__ == "__main__":
    print("-- Sistema de cobrança Klippel LTDA --")
    # Entrada de dados do usuario
    print("")
    prestacao = float(input("Digite o valor da prestação R$ "))
    dias_atraso = int(input("Digite quantos dias a prestação esta em atraso: "))
    taxa_mensal = int(input("Digite a taxa de juros mensal % "))

    # Criar um objeto do sistema de cobrança
    cobranca = SistemaCobranca(prestacao, dias_atraso, taxa_mensal)

    # Calcular o juros e valor total
    juros = cobranca.calcular_valor_juros()
    total = cobranca.calcular_valor_total()

    # Exibir os resultados formatados
    print("")
    print(f"Valor da prestação R$ {prestacao:.2f}")
    print(f"Dias em atraso: {dias_atraso:.2f}")
    print(f"Taxa do juros cobrado % {taxa_mensal:.2f}")
    print(f"Valor do juros cobrado R$ {juros:.2f}")
    print(f"Valor final da prestação R$ {total:.2f}")