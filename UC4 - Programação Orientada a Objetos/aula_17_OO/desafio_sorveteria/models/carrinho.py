from models.produto import Produto

class Carrinho:
    # Dicionario privado que mapeia Produto -> quantidade
    def __init__(self):
        self.__itens: dict[Produto,int]= {}

    def adicionar(self,produto:Produto,quantidade:int) -> None:
        '''Adiciona um produto no carrinho.
        Validações:
        - quantidade precisa ser > 0
        - precisa haver estoque suficiente no produto
        - se tudo estiver ok, o estoque é reduzido e  o carrinho
        é atualizado'''
        quantidade=int(quantidade)

        if quantidade<=0:
            raise ValueError("Quantidade deve ser maior que zero.")
        if quantidade>produto.estoque:
            raise ValueError(f"Estoque insufuciente! Disponível: {produto.estoque}")
        
        # Reserva as unidades no estoque do produto
        produto.reduzir_estoque(quantidade)

        # Atualiza o carrinho somando com o que ja existe
        if produto in self.__itens:
            self.__itens[produto]+=quantidade
        else:
            self.__itens[produto]=quantidade

    def remover(self,produto:Produto,quantidade:int) -> None:
        '''Remove unidades de um produto do carrinho
        
        Regras:
        - se remover tudo (ou mais di que há no carrinho), o
        item é excluido do carrinho.
        - Sempre devolvendo a quantidade removida ao estoque
        do produto'''

        quantidade- int(quantidade)
        if quantidade <=0:
            raise ValueError("Quantidade para remover deve ser maior que zero.")
        
        if produto in self.__itens:
            qtd_no_carrinho = self.__itens[produto]

            if quantidade>= qtd_no_carrinho:
                # Devolve todas as unidades ao estoque e remove
                # o item do carrinho
                produto.aumentar_estoque(qtd_no_carrinho)
                del self.__itens[produto]
            else:
                # Devolve apenas parte ao estoque e atualiza
                # o carrinho
                self.__itens[produto] -= quantidade
                produto.aumentar_estoque(quantidade)
    
    def listar_itens(self):
        return self.__itens.items()
    
    def calcular_total(self) -> float:
        '''Calcula o valor total (soma de preço * quantidade
        de cada item)'''
        return sum(produto.preco * qtd for produto, qtd in self.__itens.items())
    
    def total_itens(self) -> int:
        '''Quantidade total de unidades no carrinho'''
        return sum(qtd for qtd in self.__itens.values())
    
    def vazio(self) ->bool:
        '''Retorna True se o carrinho não tem itens,
        caso contrário retorna false'''
        return len(self.__itens) == 0
    