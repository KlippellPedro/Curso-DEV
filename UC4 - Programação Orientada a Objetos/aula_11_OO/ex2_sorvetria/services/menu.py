from models.picole import Picole

class Menu:
    def __init__(self):
        self.sabores=[
            Picole(1, "Uva",1.00),
            Picole(2, "Laranja",1.25),
            Picole(3, "Milho",1.50),
            Picole(4, "Coco Queimado",1.80),
            Picole(5, "Tamrindo",2.00)
        ]

    def exibir_menu_picole(self):
        print("\n-- Sorveteria Klippel LTDA --\n")
        print("--- Menu de Picolés ---")
        for picole in self.sabores:
            print(f"{picole.codigo} - {picole.nome} - R$ {picole.preco:.2f}")

    def obter_picole_por_codigo(self,codigo):
        for picole in self.sabores:
            if picole.codigo== codigo:
                return picole
            
        return None
    
    def exibir_menu_pagamento(self):
        print("\n-- Menu de pagamento --\n")
        print("1 - Dinehrio ou Pix - 10% de desconto")
        print("2 - Cartão de débito - 5% de desconto")
        print("3 - Cartão de crédito 30 dias - Mesmo valor")
        print("4 - Cartão de crédito em 2x - 5% de acréscimo")
        print("5 - Cartão de crédito em 3x - 10% de acréscimo")
        print("6 - Cartão de crédito em 4x - 15% de acréscimo")
