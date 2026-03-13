class Pagamento:
    def __init__(self,total):
        self.__total=total
        self.__parcelamento=0.0

    @property 
    def total(self):
        return self.__total

    @property
    def parcelamento(self):
        return self.__parcelamento

    def aplicar_pagaemnto(self,opcao):
        if opcao==1:
            self.__total*=.90
            print("Desconto de 10% aplicado")
        elif opcao==2:
            self.__total*=.95
            print("Desconto de 5% aplicado")
        elif opcao==3:
            print("Pagamento no cartão de crédito em 30 dias - Mesmo valor")
        elif opcao==4:
            self.__total*=1.05
            self.__parcelamento= self.__total/2
            print(f"Acréscimo de 5%. parcelado em 2x de R$ {self.__parcelamento:.2f}")
        elif opcao==5:
            self.__total*=1.10
            self.__parcelamento= self.__total/3
            print(f"Acréscimo de 10%. parcelado em 3x de R$ {self.__parcelamento:.2f}")
        elif opcao==6:
            self.__total*=1.15
            self.__parcelamento= self.__total/4
            print(f"Acréscimo de 15%. parcelado em 4x de R$ {self.__parcelamento:.2f}")

    def exibir_total(self):
        print(f"Valor total da compra R$ {self.__total:.2f}")
    