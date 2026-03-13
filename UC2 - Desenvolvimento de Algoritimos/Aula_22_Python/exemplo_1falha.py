# Sistema para uma loja de brinquedos antigos
def exibir_menu_mercado():
    print("-- Loja de Brinquedos GR!TTA --")
    print("")
    print("--- Menu de Brinquedos ---")
    print("")
    print("1- Carrinho de Controle Remoto Super Máquina R$ 500,00")
    print("2- Boneca Barbie R$ 450,00")
    print("3- Boneco Cobra Comando em Ação R$ 300,00")
    print("4- Boneco Fofão R$ 480,00")
    print("5- Videogame Atari R$ 820,00")
    print("6- Jogo Super Mário R$ 100,00")
    print("7- Bicicleta Caloi Cross Extra R$ 5.000,00")

def obter_preco_produto(opcao):
    produtos = {
        1: ("Carrinho de Controle Remoto Super Máquina", 500.00),
        2: ("Boneca Barbie", 450.00),
        3: ("Boneco Cobra Comando em Ação", 300.00),
        4: ("Boneco Fofão", 480.00),
        5: ("Videogame Atari", 820.00),
        6: ("Jogo Super Mário", 100.00),
        7: ("Bicicleta Caloi Cross Extra", 5000.00)
    }
    return produtos.get(opcao, (None, 0))

def realizar_compra():
    total = 0.0
    quantidade_total = 0
    compras = []
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
            compras.append({
                "nome": nome_produto,
                "quantidade": quantidade,
                "preco_unitario": preco
            })
            subtotal = preco *quantidade
            total += subtotal
            quantidade_total += quantidade
            print("")
            print(f"Você comprou {quantidade} unidade(s) de {nome_produto}")
            print(f"Subtotal da compra R$ {subtotal:.2f}")
            print(f"Total cumulado R$ {total:.2f}")
            print("")
        except ValueError:
            print("Entrada inválida! Digite um número Válido.")
            continue
        continuar = input("Deseja continuar comprando (S/N): ")
    return total, quantidade_total, compras

def exibir_menu_pagamento():
    print("--- Menu de Opções de Pagamento ---")
    print("1 - A vista em dinheiro ou PIX, 5% de desconto")
    print("2 - No cartão de débito - mesmo valor")
    print("3 - No cartão de crétido em 1x - acréscimo de 5%")
    print("4 - No cartão de crédito em 2x - acréscimo de 6%")
    print("5 - No cartão de crédito em 3x - acréscimo de 8%")
    print("6 - No cartão de crédito em 4x - acréscimo de 9%")
    print("7 - No cartão de crédito em 5x - acréscimo de 10%")

def aplicar_pagamento(total):
    while True:
        try:
            exibir_menu_pagamento()
            print("")
            opcao = int(input("Escolha uma das opções de pagamento: "))
            print("")
            if opcao == 1:
                desconto = total *0.5
                total -= desconto
                print(f"Desconto de 5% aplicado -R$ {desconto:.2f}")
            elif opcao == 2:
                print("Pagamento sem desconto ou acréscimo.")
            elif opcao == 3:
                acrescimo = total *0.05
                total += acrescimo
                print(f"Acréscimo de 5% aplicado +R$ {acrescimo:.2f}")
                print(f"Parcelado em 1x de R$ {total /1:.2f}")
            elif opcao == 4:
                acrescimo = total *0.06
                total += acrescimo
                print(f"Acréscimo de 6% aplicado +R$ {acrescimo:.2f}")
                print(f"Parcelado em 2x de R$ {total /2:.2f}")
            elif opcao == 5:
                acrescimo = total *0.08
                total += acrescimo
                print(f"Acréscimo de 8% aplicado -R$ {acrescimo:.2f}")
                print(f"Parcelado em 3x de R$ {total /3:.2f}")
            elif opcao == 6:
                acrescimo = total *0.09
                total += acrescimo
                print(f"Acréscimo de 9% aplicado -R$ {acrescimo:.2f}")
                print(f"Parcelado em 4x de R$ {total /4:.2f}")
            elif opcao == 7:
                acrescimo = total *0.10
                total += acrescimo
                print(f"Acréscimo de 10% aplicado -R$ {acrescimo:.2f}")
                print(f"Parcelado em 5x de R$ {total /5:.2f}")
            else:
                print("Opção de pagamento inválida! Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Digite um número válido")
    return total

def main():
    quantidade_dia = 0.0
    valor_dia = 0.0
    novo_cliente = "s"
    while novo_cliente.lower() == "s":
        total, quantidade_total, compras = realizar_compra()
        total_final = aplicar_pagamento(total)
        print(f"Quantidade total de produtos comprados: {quantidade_total} unidade(s).")
        print(f"Valor total da compra R$ {total_final:.2f}")
        print("\n--- Resumo da Compra ---")
        print("")
        for item in compras:
            subtotal = item["quantidade"] * item["preco_unitario"]
            print(f"{item['quantidade']}x {item['nome']}     /     R${item['preco_unitario']:.2f} unidade(s)     /     Subtotal R$ {subtotal:.2f}")
        quantidade_dia += quantidade_total
        valor_dia += total_final 
        novo_cliente = input("Deseja cadastrar um novo cliente (S/N): ")
        print(f"Total de produtos vendidos no dia: {quantidade_dia}")
        print(f"Vlaor total arrecadado: {valor_dia}")
    
    

if __name__ == "__main__":
    main()