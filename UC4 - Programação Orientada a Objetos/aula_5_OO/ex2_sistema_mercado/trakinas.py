class VendaTrakinas:
    '''
    Classe para representar uma venda de takinas, calcular o valor
    total com desconto para compras acima de 20 unidades
    '''
    def __init__(self,quantidade):
        # Inicializa com a quantidade de unidades compradas
        self.quantidade = quantidade
        # Preço padrão por unidade (menos de 20 unidades)
        self.preco_unitario = 4.5
        # Preço com desconto por unidade (20 ou mais unidades)
        self.preco_desconto=4.0

    def calcular_valor_total(self):
        '''
        Calcula o valor total da compra, considerando o desconto
        para compras acima de 20 unidades
        '''
        if self.quantidade >=20:
            return self.quantidade*self.preco_desconto
        else:
            return self.quantidade*self.preco_unitario
        
    def informar_preco_unitario(self):
        '''
        Retorna o preço unitario aplicavel conforme a quantidade
        '''
        if self.quantidade>=20:
            return self.preco_desconto
        else:
            return self.preco_unitario