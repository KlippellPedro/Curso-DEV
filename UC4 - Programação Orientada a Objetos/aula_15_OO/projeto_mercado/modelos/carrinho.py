from modelos.produto import Produto
class Carrimho:
    def __init__(self):
        self._itens=[]

    def adicionar_itens(self,produto,quantidade):
        '''Adiciona um item ao carrinho, verificando a validade da
        quantidade e a disponibilidade em estoque'''
        if quantidade<=0:
            raise ValueError("A quantidade deve ser maior que zero.")
        
        if quantidade>produto.estoque:
            raise ValueError("Estoque insuficiente para este produto.")
        # Adicionar o item (produto e quantidade) a lista _itens
        self._itens.append(produto,quantidade)
        # Reduz o estoque do produto
        produto.reduzir_estoque(quantidade)

    def calcular_total(self):
        '''Calcula o valor total do carrinho'''
        return sum(produto.preco*quantidade for produto,quantidade in self._itens)
    
    def listar_itens(self):
        '''Exibe uma lista de todos os itens no carrinho com suas 
        respectivas quantidades e preços'''
        for produto,quantidade in self._itens:
            print(f"{quantidade}x {produto.nome} - R$ {produto.preco:.2f} cada")

    def total_itens(self):
        '''Retorna o número total de itens (unidades) no carrinho'''
        return sum(quantidade for _,quantidade in self._itens)
