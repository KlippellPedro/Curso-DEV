# Sistema para um mercado
total = 0
quantTotal = 0
totaldia = 0.0
produtodia = 0
op = "s"
opp = "s"
while op.lower() == "s":
    total = 0
    quantTotal = 0
    while op.lower() == "s":
        print("-- Mercado do haha --")
        print("# Menu de opções #")
        print("1 - Arroz R$ 5,00")
        print("2 - Feijão R$ 7,50")
        print("3 - Leite R$ 4,00")
        print("4 - Café R$ 30,00")
        opcao = int(input("Selecione uma opção: "))
        if opcao <= 0 or opcao > 4:
            print("Você escolheu uma opção inválida!")
            print("Realize a compra novamente!")
        else:
            quantidade = int(input("Quantas unidades você deseja comprar: "))
            quantTotal += quantidade
            print("")
            if opcao == 1:
                subtotal = quantidade * 5.00
                produto = "Arroz"
            elif opcao == 2:
                subtotal = quantidade * 7.50
                produto = "Feijão"
            elif opcao == 3:
                subtotal = quantidade * 4.00
                produto = "Leite"
            elif opcao == 4:
                subtotal = quantidade * 30.00
                produto = "Café"
            print(f"Você comprou {quantidade} unidade(s) de {produto}")
            print(f"Valor da compra R$ {subtotal:.2f}")
            total += subtotal
            print(f"Valor total da sua compra até o momento R$ {total:.2f}")
        print("") 

        op = input("Deseja continuar comprando (S/N): ")
    parcelamento = 0.0         
    opPagamento = 0
    while opPagamento <= 0 or opPagamento > 6:
        print("")
        print("-- Menu de opções de pagamento --")
        print("1 - A vista em dinheiro ou PIX, 10% de desconto")
        print("2 - No cartão de débito, 5% de desconto")
        print("3 - No cartão de crétido em 1x, mesmo valor")
        print("4 - No cartão de crédito em 2x, acréscimo de 5%")
        print("5 - No cartão de crédito em 3x, acréscimo de 10%")
        print("6 - No cartão de crédito em 4x, acréscimo de 15%")
        opPagamento = int(input("Escolha uma opção de pagamento: "))
        print("")
        if opPagamento <= 0 or opPagamento > 6:
            print("Você escolheu uma opção de pagamento inválido!")
            print("Escolha novamente!")
        else:
            if opPagamento == 1:
                total -= total * 0.10
                print("Sua compra teve um desconto de 10%")
            elif opPagamento == 2:
                total -= total * 0.05
                print("Sua compra teve um desconto de 5%")
            elif opPagamento == 3:
                print("Você vai pagar o preço a vista do(s) produto(s) comprado(s)")
            elif opPagamento == 4:
                total += total * 0.05
                parcelamento = total / 2
                print(f"Sua compra teve um acréscimo de 5%, parcelado em 2x de R$ {parcelamento:.2f}")
            elif opPagamento == 5:
                total += total * 0.10
                parcelamento = total / 3
                print(f"Sua compra teve um acréscimo de 10%, parcelado em 3x de R$ {parcelamento:.2f}")
            elif opPagamento == 6:
                total += total * 0.15
                parcelamento = total / 4
                print(f"Sua compra teve um acréscimo de 15%, parcelado em 4x de R$ {parcelamento:.2f}")

            print(f"Quantidade de produtos comprados: {quantTotal} unidade(s)")
            print(f"Valor total da sua compra R$ {total:.2f}")
            print("")
            op = input("Deseja fazer uma nova compra? (S/N): ")
            print("")
            totaldia += total
            produtodia += quantTotal
            print(f"Quantidade de produtos vendidos hoje: {produtodia}")
            print(f"Total de todas as compras de hoje: {totaldia}")
