from models.picole import Picole
class Menu:
    def __init__(self):
        # Lista privada de objetos Picole disponivel para venda
        # Usamos atributo com duplo undercore para indicar privacidade
        self.__sabores=[
            Picole(1, "Menta", 1.00),
            Picole(2, "Chiclete", 1.25),
            Picole(3, "Boldo", 1.50),
            Picole(4, "Amarula", 1.75),
            Picole(1, "Python", 2.00)
        ]

    # Metodo publico que mostra o menu de picoles no console
    def exibir_menu_picoles(self):
        print("\n-- Sorveteria Klippel LTDA --")
        print("\n--- Menu de Sabores ---\n")
        for picole in self.__sabores:
            print(f"{picole.codigo} - {picole.nome} - R${picole.preco:.2f}")

    # Metodo publico que retorna o ojeto Picole correspondente ao codigo informado
    def obter_picole_por_codigo(self,codigo):
        '''Percorre a lista procurando um picole cujo atributo codigo
        bata com o informado
        '''
        for picole in self.__sabores:
            if picole.codigo==codigo:
                return picole
        return None
    
    # Metodo publico que exibe as opções de pagamentos disponiveis
    def exibir_menu_pagamento(self):
        print("\n-- Menu de Opções de Pagamento --\n")
        print("1- Dinheiro ou Pix - 10% de desconto")
        print("2 - Cartão de débito - 5% de desconto")
        print("3 - Cartão de crédito 30 dias - Mesmo valor")
        print("4 - Cartão de crédito 2x - 5% de acréscimo")
        print("5 - Cartão de crédito 3x - 10% de acréscimo")
        print("6 - Cartão de crédito 4x - 15% de acréscimo")

    