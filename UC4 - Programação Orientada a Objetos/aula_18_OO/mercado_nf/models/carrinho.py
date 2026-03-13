from models.produto import Produto

class Carrinho:
    def __init__(self):
        self.__itens={}
    
    def adicionar(self,produto:Produto,quantidade:int):
        if quantidade<=0:
            raise ValueError("Quantidade deve ser maior que zero.")
        if quantidade>produto.estoque:
            raise ValueError(f"Estoque insulficiente! Disonivel: {produto.estoque}")
        produto.reduzir_estoque(quantidade)
        if produto in self.__itens:
            self.__itens[produto]+=quantidade
        else:
            self.__itens[produto]= quantidade
    
    def remover(self,produto:Produto,quantidade=int):
        if quantidade<=0:
            raise ValueError("Quantidade inválida.")
        if produto in self.__itens[produto]:
            qtd_no_carrinho=self.__itens[produto]
            if quantidade>=qtd_no_carrinho:
                produto.aumentar_estoque(qtd_no_carrinho)
                del self.__itens[produto]
            else:
                self.__itens[produto]-= quantidade
                produto.aumentar_estoque(quantidade)

    def listar_itens(self):
        return self.__itens.items()
    def calcular_total(self):
        return sum(p.preco*qtd for p,qtd in self.__itens.items())
    def total_itens(self):
        return sum(qtd for qtd in self.__itens.values())
    def vazio(self):
        return len(self.__itens) ==0