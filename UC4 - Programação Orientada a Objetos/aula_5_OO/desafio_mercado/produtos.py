class Produtos:
    def __init__(self,quantidade,preco,nome):
        self.quantidade = quantidade
        self.preco_unitario = preco
        self.nome = nome

    def calcular_valor_total(self):
       return self.quantidade*self.preco_unitario