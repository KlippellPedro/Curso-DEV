class Pagamento:
    def __init__(self,total):
        self.total=total
        self.pagamento=0.0

    def aplicar_pagamento(self,opcao):
        if opcao==1:
            self.total*=.90
            print("Desconto de 10% aplicado- Dinheiro ou Pix")
        elif opcao==2:
            self.total*=.95
            print("Cartão de débito - 5% de desconto")
        elif opcao==3:
            print("Cartão de crédito 30 dias - Mesmo valor")
        elif opcao==4:
            self.total*=1.05
            self.parcelamento= self.total/2
            print(f"Acréscimo de 5%. Parcelado em 2x de R$ {self.parcelamento:.2f}")
        elif opcao==5:
            self.total*=1.10
            self.parcelamento= self.total/3
            print(f"Acréscimo de 10%. Parcelado em 3x de R$ {self.parcelamento:.2f}")
        elif opcao==6:
            self.total*=1.15
            self.parcelamento= self.total/4
            print(f"Acréscimo de 15%. Parcelado em 4x de R$ {self.parcelamento:.2f}")
        else:
            print("Escolha uma opção de pagamento válida!")

    def exibir_total(self):
        print(f"Valor total da compra R$ {self.total:.2f}")