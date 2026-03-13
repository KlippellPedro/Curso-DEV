from services.menu import Menu
from models.pedido import Pedido
from models.pagamento import Pagamento

class Sorveteria:
    def __init__(self):
        self.menu=Menu()
        self.pedidos= []

    def iniciar_compras(self):
        opcao= "s"
        while opcao.lower()=="s":
            self.menu.exibir_menu_picole()
            try:
                codigo=int(input("Selecione uma das opções: "))
                picole= self.menu.obter_picole_por_codigo(codigo)

                if picole is None:
                    print("Opção inválida! Tente novamente.")
                    continue

                quantidade= int(input("Informe quantos picoles deseja comprar: "))
                pedido=Pedido(picole,quantidade)
                self.pedidos.append(pedido)
                print("")
                pedido.exibir_resumo()
                print(f"Total acumulado R$ {self.calcular_total():.2f}")
                print("")

                opcao= input("Deseja continuar comprando (S/N): ")

            except ValueError:
                print("Entrada inválida! Digite números válidos")

    def calcular_total(self):
        return sum(p.calcular_subtotal() for p in self.pedidos)
    
    def calcular_quantidade_total(self):
        return sum(p.quantidade for p in self.pedidos)
    
    def processar_pagamento(self):
        total= self.calcular_total()
        pagamento=Pagamento(total)
        while True:
            try:
                self.menu.exibir_menu_pagamento()
                opcao= int(input("Escolha uma opção de pagamento: "))
                if 1<= opcao<=6:
                    pagamento.aplicar_pagamento(opcao)
                    pagamento.exibir_total()
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            except ValueError:
                print("Digite um número válido.")
        return pagamento
    
    def finalizar_compra(self):
        print("\n","-"*30,"\n")
        print(f"Quantidade total de picolés comprados: {self.calcular_quantidade_total()}")