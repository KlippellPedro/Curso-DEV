class Pedido:
    def __init__(self,picole,quantidade):
        self.__picole=picole
        self.__quantidade=quantidade

    @property
    def picole(self):
        return self.__picole
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    # Setter para quantidade com validação. Assim controlamos atribuições indevidas
    @quantidade.setter
    def quantidade(self,valor):
        if valor<=0:
            raise ValueError("A quantidade deve ser maior que zero.")
        self.__quantidade=valor

    def calcular_subtotal(self):
        return self.__picole.preco*self.__quantidade
    
    def exibir_resumo(self):
        print(f"{self.__quantidade}x Picolé de {self.__picole.nome} - R$ {self.calcular_subtotal():.2f}")