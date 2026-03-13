class LojaVeiculos:
    '''
    Final de um veiculo
    '''
    def __init__(self,nome_veiculo,preco_fabrica):
        '''
        Inicializa os dados do veiculo
        '''
        self.nome_veiculo = nome_veiculo
        self.preco_fabrica = preco_fabrica
        # Percentuais dixos de imposto e lucro do vendedor
        self.percentual_imposto = 0.45
        self.percentual_revendedor = 0.28
    def calcular_imposto(self):
        '''
        Método para calcular o valor do imposto sobre o preço de fabrica
        '''
        return self.preco_fabrica* self.percentual_imposto
    def calcular_lucro_revendedor(self):
        '''
        Método para calcular o valor do imposto sobre o preço de fabrica
        '''
        return self.preco_fabrica * self.percentual_revendedor
    def calcular_preco_final(self):
        '''
        Método para calcular o preço final do veiculo para revenda
        '''
        return self.preco_fabrica+self.calcular_imposto()+self.calcular_lucro_revendedor()
if  __name__ == "__main__":
    print("-- Loja de veículos Klippel LTDA --")
    nome = input("Informe o nome do veiculo: ")
    preco_fabrica = float(input("Digite o valor do veículo na fábrica R$ "))

    #Criar o objeto da loja
    veiculo = LojaVeiculos(nome,preco_fabrica)

    # Calculo dos valores
    imposto = veiculo.calcular_imposto()
    lucro = veiculo.calcular_lucro_revendedor()
    preco_final = veiculo.calcular_preco_final()

    print("")
    print(f"Nome do veículo: {veiculo.nome_veiculo}")
    print(f"Valor veículo na fabrica R$ {veiculo.preco_fabrica:.2f}")
    print(f"Valor do imposto cobrado do veículo R$ {imposto:.2f}")
    print(f"Valor do lucro do revendedor R$ {lucro:.2f}")
    print(f"Valor final do veículo para revenda R$ {preco_final:.2f}")