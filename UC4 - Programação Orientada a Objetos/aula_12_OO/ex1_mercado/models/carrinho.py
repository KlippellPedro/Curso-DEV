from models.produto import Produto

class Carrinho:
    def __init__(self):
        self.itens=[]
        self.total=0.0
        self.quantidade_total=0

    def adicionar_item(self,produto: Produto,quantidade:int):
        subtotal= produto.preco*quantidade
        self.itens.append((produto,quantidade,subtotal))
        self.total+=subtotal
        self.quantidade_total+=quantidade
    
    def mostrar_resumo(self):
        print("\n=== Resumo do Carrinho ===\n")
        for item in self.itens:
            produto,quantidade,subtotal=item
            print(f"{quantidade}x {produto.nome}- Subtotal R$ {subtotal:.2f}")
        print(f"Quantidade total de itens: {self.quantidade_total}")
        print(f"Valor total R$ {self.total:.2f}")
        print("\n","-"*30,"\n")
