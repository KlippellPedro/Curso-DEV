class Produto:
    def __init__(self,nome:str,preco:float,estoque:int=10):
        self._nome=nome
        self._preco= float(preco)
        self._estoque= int(estoque)

    @property
    def nome(self): return self._nome
    @property
    def preco(self): return self._preco
    @property
    def estoque(self): return self._estoque
    
    def reduzir_estoque(self,quantidade:int):
        if quantidade<=0:
            raise ValueError("Quantidade deve ser positiva.")
        if quantidade>self._estoque:
            raise ValueError("Estoque insuficiente!")
        self._estoque-=quantidade

    def aumentar_estoque(self,quantidade:int):
        if quantidade<=0:
            raise ValueError("Quantidade deve ser positiva.")
        self._estoque+=quantidade
        
    def __str__(self):
        return f"{self._nome} - R$ {self._preco:.2f} (Estoque: {self._estoque})"
    