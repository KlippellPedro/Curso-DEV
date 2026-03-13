from services.menu import Menu
from models.pedido import Pedido
from models.pagamento import Pagamento

class Sorveteria:
    def __init__(self):
        self.__menu=Menu()
        self.__pedidos=[]

    @property
    def pedidos(self):
        return self.__pedidos
    
    def iniciar_compras(self):
        opcao="s"
        while opcao.lower()== "s":
            self.__menu.exibir_menu_picoles()
            try:
                codigo=int(input("Selecione uma opção: "))
                picole= self.__menu.obter_picole_por_codigo(codigo)

                if picole is None:
                    print("Opção inválida! Tente novamente.")
                    continue

                quantidade= int(input("Quantos picolés deseja comprar: "))
                pedido= Pedido(picole,quantidade)
                self.__pedidos.append(pedido)

                print("\n","-"*30,"\n")
                pedido.exibir_resumo()
                print(f"Total acumulado R$ {self.calcular_total():.2f}")
                print("\n","-"*30,"\n")
                opcao= input("Deseja continuar comprado (S/N): ")

            except ValueError:
                print("Entrada inválida! Digite números válidos.")
    
    def calcular_total(self):
        return sum(p.calcular_subtotal() for p in self.__pedidos)
    
    def calcular_quantidade_total(self):
        return sum(p.quantidade for p in self.__pedidos)
    
    def processar_pagamento(self):
        total=self.calcular_total()
        pagamento=Pagamento(total)
        while True:
            try:
                self.__menu.exibir_menu_pagamento()
                opcao=int(input("Escolha uma opção de pagamento: "))
                if 1<= opcao<=6:
                    pagamento.aplicar_pagaemnto(opcao)
                    pagamento.exibir_total()
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            except ValueError:
                print("Digite um número válido.")
        return pagamento
    
    def finalizar_compra(self):
        print("\n","-"*30,"\n")
        print(f"Quantidade de picolés comprados: {self.calcular_quantidade_total()}")
        print(f"A corporação Klippel LTDA, agradece sua preferência.")