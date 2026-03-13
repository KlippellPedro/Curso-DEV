class Pagamento:
    def __init__(self,total:float):
        self.total=float(total)

    def calcular_pagamento(self,opcao: int) -> tuple[float,str]:
        if opcao==1:
            return self.total*0.90, "Dinheiro ou Pix - 10% de desconto"
        elif opcao == 2:
            return self.total*0.95, "Cartão de débito - 5% de desconto"
        elif opcao == 3:
            return self.total*0.90, "Crédito à vista - Mesmo valor"
        elif opcao == 4:
            return self.total*1.05, "Crédito 2x - 5% de acréscimo"
        elif opcao == 5:
            return self.total*1.10, "Crédito 3x - 10% de acréscimo"
        elif opcao == 6:
            return self.total*1.15, "Crédito 4x - 15% de acréscimo"
        else:
            raise ValueError("Opção inválida de pagamento.")