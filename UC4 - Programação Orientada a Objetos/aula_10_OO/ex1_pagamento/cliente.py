'''
Classe responsavel por armazenar os dados do cliente
'''
class Cliente:
    def __init__(self,nome: str, valor_compra:float):
        # Construtor da classe
        self.nome=nome
        self.valor_compra=valor_compra

    def exibir_dados(self):
        '''
        Método responsável po exibir os dados do cliente
        '''
        print(f"Nome do cliente: {self.nome}")
        print(f"Valor da compra R$ {self.valor_compra:.2f}")