class Pagamento:

    def __init__(self,nome,valor,quantidade,opcao):
        self.nome= nome
        self.valor= valor
        self.quantidade= quantidade
        self.opcao= opcao
        

    def valor_pagamento(self):
        
        if self.opcao== 1:
            return self.valor-(self.valor*.15)
        elif self.opcao== 2:
            return self.valor-(self.valor*.1)
        elif self.opcao== 3:
            return self.valor
        elif self.opcao== 4:
            return self.valor+(self.valor*.1)

    def opcao_pagamento(self):
        
        if self.opcao== 1:
            return "Á vista em dinheiro ou pix - 15% de desconto"
        elif self.opcao== 2:
            return "Á vista no cartão de débito - 10% de desconto"
        elif self.opcao== 3:
            return "Parcelado em 2X - Preço normal"
        elif self.opcao== 4:
            return "Parcelado em 3X - 10% de acrèscimo"