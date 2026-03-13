from models.produto import Produto
from models.carrinho import Carrinho
from models.pagamento import Pagamento

class MercadoController:
    def __init__(self):
        self.produtos=self.criar_produtos()
        self.total_arrecadado=0.0
        self.total_itens=0

    def criar_produtos(self):
        return{
            1:Produto("Arroz 1Kg",5.00),
            2:Produto("Feijão 1Kg",7.50),
            3:Produto("Leite 1L",4.00),
            4:Produto("Café 500 Gr",30.00)
        }
    def exibir_menu_produtos(self):
        print("\n--- Menu de Produtos ---\n")
        for codigo,produto in self.produtos.items():
            print(f"[{codigo}] {produto.nome} - R$ {produto.preco:.2f}")
        print("\n","-"*30,"\n")
    
    def exibir_menu_pagamento(self):
        print("\n--- Forma de Pagamento ---\n")
        print("1- A vista em dinheiro ou Pix - 10% de desconto")
        print("1- Cartão de débito - 5% de desconto")
        print("1- Cartão de crédito 30 dias - mesmo valor")
        print("1- Cartão de crédito 2x - 5% de acréscimo")
        print("1- Cartão de crédito 3x - 10% de acréscimo")
        print("1- Cartão de crédito 4x - 15% de acréscimo")
        print("\n","-"*30,"\n")
    
    def atender_cliente(self):
        carrinho=Carrinho()
        continuar="s"

        while continuar.lower()=="s":
            self.exibir_menu_produtos()
            try:
                codigo=int(input("Escolha o produto: "))
                if codigo not in self.produtos:
                    print("Produto inválido!")
                    continue
                quantidade=int(input("Informe a quantidade: "))
                carrinho.adicionar_item(self.produtos[codigo],quantidade)
                carrinho.mostrar_resumo()

                continuar=input("Deseja adicionar mais produtos (S/N): ")
            except ValueError:
                print("Entrada inválida! Tente novamente.")
    
        self.exibir_menu_pagamento()

        while True:
            try:
                opcao=int(input("Escolha a forma de pagamento: "))
                pagamento=Pagamento(carrinho.total)
                valor_final,descricao=pagamento.calcular_pagamento(opcao)
                break
            except (ValueError,KeyError):
                print("Opção inválida! Escolha novamente.")
        print("--- Fechamento do Pedido ---")
        carrinho.mostrar_resumo()
        print(f"Forma de pagamento: {descricao}")
        print(f"Valor total a pagar R$ {valor_final}")
        print("\n","-"*30,"\n")

        self.total_arrecadado+=valor_final
        self.total_itens+=carrinho.quantidade_total
    
    def fechar_caixa(self):
        print("--- Fechamento do Caixa ---")
        print(f"Total de itens vendidos no dia: {self.total_itens} unidade(s)")
        print(f"Total arrecadado no dia R$ {self.total_arrecadado:.2f}")
        print("\n","-"*30,"\n")