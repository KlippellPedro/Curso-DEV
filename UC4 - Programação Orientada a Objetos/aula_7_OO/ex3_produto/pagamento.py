from produto import Produto

class Pagamento:
    def __init__(self,produto:Produto, opcao_pagamento: int):
        # Armazenar o objeto Produto
        self.produto= produto
        # Armazenar a opção de pagamento escolhida (1 a 4)
        self.opcao= opcao_pagamento
        # Inicializa as variaveis para armazenar o resultado do calculo
        self.total=0.0
        self.mensagem= ""
        self.parcelas=None

    def calcular(self):
        if self.opcao==1:
            # Desconto de 15% para pagamento
            self.total= (self.produto.preco_unitario*0.85)*self.produto.quantidade
            self.mensagem= "15% de desconto sobre o valor total da compra"
        elif self.opcao==2:
            # Desconto de 10% para pagamento
            self.total= (self.produto.preco_unitario*0.90)*self.produto.quantidade
            self.mensagem= "10% de desconto sobre o valor total da compra"
        elif self.opcao==3:
            # Preço normal sem desconto ou acréscimo, parcelado em 2X
            self.total= self.produto.preco_unitario*self.produto.quantidade
            self.parcelas=2
            self.mensagem= "O cliente vai pagar o preço normal"
        elif self.opcao==4:
            # Acréscimo de 10% para parcelamento em 3X
            self.total= (self.produto.preco_unitario*1.10)*self.produto.quantidade
            self.parcelas=3
            self.mensagem= "O cliente escolheu parcelar em 3X, com acréscimo de 10%"
        else:
            # Caso a opção seja inválida
            self.mensagem= "Opção de pagamento inválida!"
            self.total= 0.0
            self.parcelas= None

        return self.total