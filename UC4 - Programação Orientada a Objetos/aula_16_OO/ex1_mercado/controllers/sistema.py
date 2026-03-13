'''Exibir produtos e estoque
- Recebe a escolha do usuario
- Controla o caminho (adicionar e remover)
- Calcula total e processa pagamento
- Registra a venda no caixa'''

from models.produto import Produto
from models.carrinho import Carrinho
from models.pagamento import Pagamento
from models.caixa import Caixa

class Sistema:
    def __init__(self):
        '''Cria a lista de produtos
        Instância do objeto de Caixa (para somar as vendas do dia)'''
        self.produtos =[
            Produto("Arroz 1Kg", 5.00),
            Produto("Feijão 1Kg", 7.50),
            Produto("Leite 1L", 4.00),
            Produto("Café 500g", 6.00),
        ]
        self.caixa= Caixa()

    def exibir_menu_produtos(self) -> None:
        '''Mostra a lista de produtos com indice (posição),
        preço e estoque.
        Tambem exibe as opções especiais:
        remover item (0) e finalizar (9)'''

        print("--- Produtos Disponíveis ---")
        for idx, produto in enumerate(self.produtos, start=1):
            print(f"[{idx}] {produto}")
        print("[0] Remover item do carrinho")
        print("[9] Finalizar compra")

    def escolher_produtos(self,opcao:int) -> Produto | None:
        '''Dados um numero digitado pelo usuário, retorna
        o Produto correspondente.
        Retorna None se a opção for inválida'''
        if 1<= opcao<= len(self.produtos):
            return self.produtos[opcao-1]
        return None
    
    def processo_compra(self) -> None:
        '''Conduz a experiência de compra de um cliente do
        inicio ao fim
        - Cria o carrinho
        - Exibe o menu e lê opções repetidamente
        - Adiciona e remove produtos
        - Quando o usuario escolhe finalizar (9),
        vai para pagamento'''
        carrinho= Carrinho()

        while True:
            # Exibe o catálogo + estoque atualizado a cada interação
            self.exibir_menu_produtos()

            # Lê a opção digitada com tratamento de erro
            try:
                opcao= int(input("Escolha a opção: "))
            except ValueError:
                print("Digite um número válido.")
                continue

            # Finaliza compra (ir para pagamento)
            if opcao==9:
                if carrinho.vazio():
                    print("O carrinho está vazio! Adicione itens antes de finalizar.")
                else:
                    break
            
            # Remove item do carrinho
            elif opcao ==0:
                self.remover_do_carrinho(carrinho)
                continue

            # Escolha de um produto do menu
            produto = self.escolher_produtos(opcao)
            if produto:
                try:
                    qtd= int(input(f"Quantos '{produto.nome}' deseja adicionar: "))
                    # Tenta adicionar ao carrinho; se faltar estoque, levanta  ValueError
                    carrinho.adicionar(produto,qtd)
                    print(f"{qtd}x '{produto.nome}' adicionados ao carrinho.")
                except ValueError as e:
                    print(e)

            else:
                print("Opção inválida! Selecione um número do menu.")
            
        self.finalizar_compra(carrinho)
    
    def remover_do_carrinho(self,carrinho: Carrinho) -> None:
        '''Permite que o cliente'''
        if carrinho.vazio():
            print("O carrinho está vazio, não há irtens para nemover")
            return
        
        print("--- Itens no Carrinho ---")
        itens= list(carrinho.listar_itens())
        for idx, (produto,qtd) in enumerate(itens,start=1):
            print(f"[{idx}] {produto.nome} - {qtd} unidade(s)")
        
        try:
            opcao = int(input("Escolha o item que deseja remover: "))
            if 1 <= opcao <= len(itens):
                produto,qtd_no_carrinho = itens[opcao-1]
                qtd_remover = int(input(f"Quantas unidades deseja remover de '{produto.nome}'?"))
                if qtd_remover >0:
                    carrinho.remover(produto,qtd_remover)
                    print(f"{qtd_remover}x '{produto.nome}' removidos do carrinho.")
                else:
                    print("Quantidade inválida (precisa ser maior que zero.)")
            
            else:
                print("Opção inválida! Selecione um indice da lista.")
            
        except ValueError:
            print("Digite um número valido.")
    
    def finalizar_compra(self,carrinho: Carrinho) -> None:
        '''Calcula o total do carrinho, apresenta as formas de pagamento,
        aplica o desconto ou acréscimo e registra a venda no caixa'''

        total = carrinho.calcular_total()

        print("--- Formas de pagamento ---")
        print("[1] Dinheiro ou Pix - 10% de desconto")
        print("[2] Cartão de débito - 5% de desconto")
        print("[3] Cartão de crédito 1x - sem desconto ou acréscimo")
        print("[4] Cartão de crédito 2x - 5% de acréscimo")
        print("[5] Cartão de crédito 3x - 10% de acréscimo")
        print("[6] Cartão de crédito 4x - 15% de acréscimo")

        # Valida a forma de pagamento
        while True:
            try:
                opcao= int(input("Escolha a forma de pagamento: "))
                pagamento= Pagamento(total)
                valor_final,forma = pagamento.calcular_pagamento(opcao)
                break
            except (ValueError,Exception):
                print("Opção inválida! Tente novamente.")
        
        # Exibe o resumo claro da compra
        print("==== Resumo da Compra ====")
        for produto,qtd in carrinho.listar_itens():
            print(f"{qtd}x {produto.nome} - R$ {produto.preco*qtd:.2f}")
        print(f"Forma de pagamento: {forma}")
        print(f"Total a pagar R$ {valor_final:.2f}")

        # Atualiza o caixa do dia (relatorio)
        self.caixa.registrar_venda(valor_final, carrinho.total_itens())

    def fechamento_dia(self) -> None:
        '''Aciona o relatorio do caixa (totais do dia)'''
        print("--- Fechamento do Dia ---")
        self.caixa.fechamento()