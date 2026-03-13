class Corretora:

    def __init__(self,nome,valor_imovel):
        self.nome= nome
        self.valor_imovel= valor_imovel
        

    def calculo_comissao(self):
        
        if self.valor_imovel>= 100000:
            return self.valor_imovel*0.20
        elif self.valor_imovel>= 75000:
            return self.valor_imovel*0.15
        else:
            return self.valor_imovel*0.10
        