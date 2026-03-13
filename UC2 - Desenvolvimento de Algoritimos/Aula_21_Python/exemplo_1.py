
# Sistema para uma sorveteria
def exibir_menu_picoles():
    print("-- Sorveteria --")
    print("")
    print("--- Menu de sabores dos picolés ---")
    print("1- Picolé de Uva R$ 1,00")
    print("2- Picolé de Laranja R$ 1,25")
    print("3- Picolé de Milho R$ 1,50")
    print("4- Picolé de Coco queimado R$ 1,80")
    print("5- Picolé de Tamarindo R$ 2,00")

def obter_preco_sabor(opcao):
    # Retorna o nome e o preço do picole conforme a opção
    sabores = {
        1: ("Uva", 1.00),
        2: ("Laranja", 1.25),
        3: ("Milho", 1.50),
        4: ("Coco queimado", 1.80),
        5: ("Tamarindo", 2.00)
    }
    return sabores.get(opcao, (None, 0))

def realizar_compra():
    total = 0.0
    quantidade_total = 0
    continuar = "s"

    while continuar.lower() == "s":
        exibir_menu_picoles()
        try:
            opcao = int(input("Selecione uma das opções: "))
            nome_picole, preco = obter_preco_sabor(opcao)

            if nome_picole is None:
                print("Opção inválida! Tente novamente.")
                continue
            quantidade = int(input("Quantos picolés você deseja comprar: "))
            subtotal = preco *quantidade
            total += subtotal
            quantidade_total += quantidade

            print(f"Você comprou {quantidade} unidade(s) do picolé de {nome_picole}")
            print(f"Subtotal da compra R$ {subtotal:.2f}")
            print(f"Total cumulado R$ {total:.2f}")
        except ValueError:
            print("Entrada inválida! Digite um número Válido.")
            continue

        continuar = input("Deseja continuar comprando (S/N): ")

    return total, quantidade_total

def exibir_menu_pagamento():
    # Exibe as opções de pagamento
    print("-- Menu de opções de pagamento --")
    print("1 - A vista em dinheiro ou PIX, 10% de desconto")
    print("2 - No cartão de débito, 5% de desconto")
    print("3 - No cartão de crétido em 30 dias - mesmo valor")
    print("4 - No cartão de crédito em 2x - acréscimo de 5%")
    print("5 - No cartão de crédito em 3x - acréscimo de 10%")
    print("6 - No cartão de crédito em 4x - acréscimo de 15%")

def aplicar_pagamento(total):
    # Calcular o valor final com base na forma de pagamento
    while True:
        try:
            exibir_menu_pagamento()
            opcao = int(input("Escolha uma das opções de pagamento: "))

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
    # Função principal do programa
    total, quantidade_total = realizar_compra()
    print("")
    print(f"Quantidade total de picolés comprados: {quantidade_total} unidades.")
    total_final = aplicar_pagamento(total)
    print(f"Valor total da compra R$ {total_final:.2f}")
    print("\n Obrigado pela sua compra! Volte sempre.")

if __name__ == "__main__":
    main()