from datetime import datetime

def exibir_menu_picoles():
    print("--- Sorveteria ---")
    print("-- Menu de sabores --")
    print("1 - Picolé de Uva R$ 1,00")
    print("2 - Picolé de Laranja R$ 1,25")
    print("3 - Picolé de Milho R$ 1,50")
    print("4 - Picolé de Coco queimado R$ 1,80")
    print("5 - Picolé de tamarino R$ 2,00")

def obter_preco_sabor(opcao):
    sabores = {
        1: ("Uva", 1.00),
        2: ("Laranja", 1.25),
        3: ("Milho", 1.50),
        4: ("Coco queimado", 1.80),
        5: ("Tamarino", 2.00)
    }
    return sabores.get(opcao, (None, 0))

def realizar_compra():
    total = 0.0
    quantidade_total = 0
    continuar = "s"
    lista_compras = []

    while continuar.lower() == "s":
        exibir_menu_picoles()
        try:
            opcao = int(input("Selecione uma das opções: "))
            nome_picole, preco = obter_preco_sabor(opcao)

            if nome_picole is None:
                print("Opção inválida! Tente novamente.")
                continue

            quantidade = int(input("Quantos picolés deseja comprar: "))
            subtotal = preco * quantidade
            total += subtotal
            quantidade_total += quantidade
            lista_compras.append(nome_picole, quantidade, subtotal)

            print(f"Você comprou {quantidade} unidade(s) do picolé de {nome_picole}")
            print(f"Subtotal R$ {subtotal:.2f}")
            print(f"Total acumulado R$ {total:.2f}")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            continue

        continuar = input("Deseja continuar comprando (S/N): ")

    return total, quantidade_total, lista_compras

def exibir_menu_pagamento():
    print("\n-- Menu de forma de pagamento --")
    print("1 - A vista em dinheiro ou PIX, 10% de desconto")
    print("2 - No cartão de débito, 5% de desconto")
    print("3 - No cartão de crétido em 1x - mesmo valor")
    print("4 - No cartão de crédito em 2x - acréscimo de 5%")
    print("5 - No cartão de crédito em 3x - acréscimo de 10%")
    print("6 - No cartão de crédito em 4x - acréscimo de 15%")