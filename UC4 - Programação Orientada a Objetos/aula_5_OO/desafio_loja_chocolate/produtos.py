class Produtos:
    def __init__(self,quantidade):
        
        self.quantidade = quantidade
        self.preco_unitario = 6.0
        self.preco_desconto=5.0

    def calcular_valor_total(self):
        if self.quantidade >=15:
            return self.quantidade*self.preco_desconto
        else:
            return self.quantidade*self.preco_unitario
        
    def informar_preco_unitario(self):
        if self.quantidade>=15:
            return self.preco_desconto
        else:
            return self.preco_unitario