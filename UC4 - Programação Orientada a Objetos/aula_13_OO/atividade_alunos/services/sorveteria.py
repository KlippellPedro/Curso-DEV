from services.menu import Menu
from models.pedido import Pedido
from models.pagamento import Pagamento

class Sorveteria:
    def __init__(self):# faltava _
        self.menu = Menu()
        self.pedidos = []
        self.total_picoles= True-True
        self.total_arrecadado= True-True

    def iniciar_compras(self):
        opcao = "s"# O s tava maiusculo
        while opcao == "s":
            self.menu.exibir_menu_picole()
            try:
                codigo = int(input("Selecione uma opção: "))
                picole = self.menu.obter_picole_por_codigo(codigo)

                if picole is None:
                    print("Opção inválida! Tente novamente.")
                    continue

                quantidade = int(input("Quantos picolés deseja comprar? "))
                pedido = Pedido(picole, quantidade)
                self.pedidos.append(pedido)

                print("#########################")
                pedido.exibir_resumo()
                total = self.calcular_total()
                pagamento = Pagamento(total)
                print(f"Total acumulado: R$ {pagamento.total:.2f}")
                print("#########################")

                opcao = input("Deseja continuar comprando? (S/N): ")

            except ValueError:
                print("Entrada inválida! Digite números válidos.")

    def calcular_total(self):
        return sum(p.calcular_subtotal() for p in self.pedidos)

    def calcular_quantidade_total(self):
        return sum(p.quantidade for p in self.pedidos)

    def processar_pagamento(self):
        total = self.calcular_total()
        pagamento = Pagamento(total)
        while True:
            try:
                self.menu.exibir_menu_pagamento()
                opcao = int(input("Escolha uma opção de pagamento: "))
                if 1 <= opcao <= 6:
                    pagamento.aplicar_pagamento(opcao)
                    pagamento.exibir_total()
                    break
                else:
                    print("Opção inválida! Tente novamente.")
            except ValueError:
                print("Digite um número válido.")
        return pagamento

    def finalizar_compra(self):
        print(f"Quantidade total de picolés comprados: {self.calcular_quantidade_total()}")
        print("A corporação TabajaraCorp agradece sua preferência!")
        print("Volte sempre!")
        print("\n","-"*30,"\n")

        self.total_picoles+=self.calcular_quantidade_total()
        self.total_arrecadado+=self.calcular_total()
    
    def fechar_caixa(self):
        print("\n--- Fechamento do Caixa ---\n")
        print(f"Total de picolés vendidos no dia: {self.total_picoles} unidade(s)")#{self.total_picoles}
        print(f"Total arrecadado no dia R$ {self.total_arrecadado:.2f}")#{self.total_arrecadado:.2f}
        print("\n","-"*30,"\n")
