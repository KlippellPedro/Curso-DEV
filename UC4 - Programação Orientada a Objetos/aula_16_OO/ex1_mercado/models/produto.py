class Produto:
    def __init__(self, nome: str, preco: float, estoque: int = 10):
        self._nome = nome
        self._preco = float(preco)
        self._estoque = int(estoque)

    # Criar as propriedades somente de leitura
    @property
    def nome(self) -> str:
        return self._nome

    @property
    def preco(self) -> float:
        return self._preco

    @property
    def estoque(self) -> int:
        return self._estoque

    # Criar as operações sobre o estoque
    def reduzir_estoque(self, quantidade: int) -> None:
        '''Diminuir o estoque do produto quando uma venda ou 
        reserva acontece
        A quantidade deve sser positiva
        Não pode reduzir mais do que o disponível'''
        quantidade = int(quantidade)
        if quantidade <= 0:
            raise ValueError("A quantidade para reduzir deve ser maior que zero.")
        if quantidade > self._estoque:
            raise ValueError("Estoque insuficiente!")
        self._estoque -= quantidade

    def aumentar_estoque(self, quantidade: int) -> None:
        ''''Aumentar o estoque
        Não há limites superiores aqui, pois estamos apenas devolvendo 
        unidades que já existiam, mas ainda assim validamos 
        se a quantidade é positiva'''
        quantidade = int(quantidade)
        if quantidade <= 0:
            raise ValueError("A quantidade para aumentar deve ser maior que zero.")
        self._estoque += quantidade

    def __str__(self) -> str:
        return f"{self._nome} - R$ {self._preco:.2f} (Estoque: {self._estoque})"
                    
        