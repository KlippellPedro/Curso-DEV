# Sistema para um mercado
def exibir_menu_mercado():
    print("-- MERCADO GR!TTA --")
    print("")
    print("--- Menu de produtos ---")
    print("")
    print("1- Arroz R$ 5,00")
    print("2- Feijão R$ 7,50")
    print("3- Café R$ 30,00")
def obter_preco_produto(opcao):
    produtos = {
        1: ("Arroz", 5.00),
        2: ("Feijão", 7.50),
        3: ("Café", 30.00)
    }
    return produtos.get(opcao, (None, 0))
def realizar_compra():
    total = 0.0
    quantidade_total = 0
    continuar = "s"
    while continuar.lower() == "s":
        exibir_menu_mercado()
        try:
            opcao = int(input("Selecione uma das opções: "))
            nome_produto, preco = obter_preco_produto(opcao)
            if nome_produto is None:
                print("Opção inválida! Tente novamente.")
                continue
            quantidade = int(input("Quantos produtos você deseja comprar: "))
            subtotal = preco *quantidade
            total += subtotal
            quantidade_total += quantidade
            print(f"Você comprou {quantidade} unidade(s) de {nome_produto}")
            print(f"Subtotal da compra R$ {subtotal:.2f}")
            print(f"Total cumulado R$ {total:.2f}")
        except ValueError:
            print("Entrada inválida! Digite um número Válido.")
            continue
        continuar = input("Deseja continuar comprando (S/N): ")
    return total, quantidade_total
def exibir_menu_pagamento():
    print("--- Menu de opções de pagamento ---")
    print("1 - A vista em dinheiro ou PIX, 10% de desconto")
    print("2 - No cartão de débito, 5% de desconto")
    print("3 - No cartão de crétido em 30 dias - mesmo valor")
    print("4 - No cartão de crédito em 2x - acréscimo de 5%")
    print("5 - No cartão de crédito em 3x - acréscimo de 10%")
    print("6 - No cartão de crédito em 4x - acréscimo de 15%")
def aplicar_pagamento(total):
    while True:
        try:
            exibir_menu_pagamento()
            opcao = int(input("Escolha uma das opções de pagamento: "))
            print("")
            if opcao == 1:
                desconto = total *0.10
                total -= desconto
                print(f"Desconto de 10% aplicado -R$ {desconto:.2f}")
            elif opcao == 2:
                desconto = total *0.05
                total -= desconto
                print(f"Desconto de 5% aplicado -R$ {desconto:.2f}")
            elif opcao == 3:
                print("Pagamento sem desconto ou acréscimo.")
            elif opcao == 4:
                acrescimo = total *0.05
                total += acrescimo
                print(f"Acréscimo de 5% aplicado +R$ {acrescimo:.2f}")
                print(f"Parcelado em 2x de R$ {total /2:.2f}")
            elif opcao == 5:
                acrescimo = total *0.10
                total += acrescimo
                print(f"Acréscimo de 10% aplicado -R$ {acrescimo:.2f}")
                print(f"Parcelado em 3x de R$ {total /3:.2f}")
            elif opcao == 6:
                acrescimo = total *0.15
                total += acrescimo
                print(f"Acréscimo de 15% aplicado -R$ {acrescimo:.2f}")
                print(f"Parcelado em 4x de R$ {total /4:.2f}")
            else:
                print("Opção de pagamento inválida! Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número válido")
    return total
def main():
    total, quantidade_total = realizar_compra()
    print("")
    total_final = aplicar_pagamento(total)
    print(f"Quantidade total de produtos comprados: {quantidade_total} unidades.")
    print(f"Valor total da compra R$ {total_final:.2f}")
    print("\n Obrigado pela sua compra!")
    print(" Volte sempre.")
if __name__ == "__main__":
    main()
