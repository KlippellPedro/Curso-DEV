from picole import Picole

class Menu:
    def __init__(self):
        self.opcoes = [
            Picole(1, "Uva",1.00),
            Picole(2, "Laranja",1.25),
            Picole(3, "Milho",1.50),
            Picole(4, "Coco queimado",1.80),
            Picole(5, "Tamarindo",2.00)
        ]

    def exibir_menu(self):
        print("\n-- Sorveteria Klippel LTDA --\n")
        print("--- Menu de sabores de Picolés ---")
        for picole in self.opcoes:
            print(f"{picole.codigo} - Picolé de {picole.nome} - R$ {picole.preco:.2f}")

    def obter_picole_por_codigo(self,codigo):
        for picole in self.opcoes:
            if picole.codigo==codigo:
                return picole
            return None
        