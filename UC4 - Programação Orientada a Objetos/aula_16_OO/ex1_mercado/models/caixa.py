class Caixa:
    def __init__(self):
        self.total_dia: float = 0.0
        self.itens_vendidos: int = 0

    def registrar_venda(self, total_compra: float, itens_vendidos: int) -> None:
        # Registra uma venda no caixa
        self.total_dia += float(total_compra)
        self.itens_vendidos += int(itens_vendidos)

    def fechamento(self) -> None:
        '''Exibe um pequeno relatório de fachamento do dia'''
        print("### Fechamento do caixa ###")
        print(f"Total arrecadado no dia R$ {self.total_dia:.2f}")
        print(f"Total de itens vendidos: {self.itens_vendidos}")
        print("#"*30)    
