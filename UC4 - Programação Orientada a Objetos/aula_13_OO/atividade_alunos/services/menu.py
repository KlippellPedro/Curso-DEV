from models.picole import Picole

class Menu:
    def __init__(self):
        self.sabores = [ # Faltava as virgulas
            Picole(1, "Uva", 1.00),
            Picole(2, "Laranja", 1.25),
            Picole(3, "Milho", 1.50),
            Picole(4, "Coco Queimado", 1.80),
            Picole(5, "Tamarindo", 2.00)
        ]

    def exibir_menu_picole(self):
        print("## Sorveteria TabajaraCorp ##")
        print("### Menu de Picolés ###")
        for picole in self.sabores:
            print(f"{picole.codigo} - {picole.nome} - R$ {picole.preco:.2f}")

    def obter_picole_por_codigo(self, codigo):
        for picole in self.sabores:
            if picole.codigo == codigo:
                return picole
        return None

    def exibir_menu_pagamento(self):
        print("## Menu de Pagamento ##")
        print("1 - Dinheiro ou PIX (10% de desconto)")
        print("2 - Cartão de Débito (5% de desconto)")
        print("3 - Cartão de Crédito (30 dias, sem acréscimo)")
        print("4 - Cartão de Crédito (2x, acréscimo de 5%)")
        print("5 - Cartão de Crédito (3x, acréscimo de 10%)")
        print("6 - Cartão de Crédito (4x, acréscimo de 15%)") 
