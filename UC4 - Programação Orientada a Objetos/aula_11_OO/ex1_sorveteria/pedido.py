class Pedido:
    def __init__(self,picole,quantidade):
        self.picole=picole
        self.quantidade=quantidade

    def calcular_subtotal(self):
        return self.picole.preco*self.quantidade
    
    def exibir_resumo(self):
        subtotal=self.calcular_subtotal