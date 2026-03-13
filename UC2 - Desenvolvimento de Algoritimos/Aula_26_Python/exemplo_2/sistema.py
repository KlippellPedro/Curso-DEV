from menu import exibir_menu_principal, exibir_formas_pagamento
from calculos import calcular_subtotal, calcular_pagamento

def sistema_caixa():
    total_arrecadado_dia = 0.0
    total_itens_vendidos = 0
    novo_cliente = "s"

    while novo_cliente.lower() == "s":
        total = 0.0
        quant_total = 0
        sn = "s"
        print("-- Mercado Guaxilandia --")

        while sn.lower() == "s":
            exibir_menu_principal()
            try:
                opcao = int(input("Selecione uma das opções: "))
                if opcao not in [1, 2, 3, 4, 5]:
                    print("Você escolheu uma opção inválida!")
                    continue
                quantidade = int(input("Quantos produtos deseja adicionar: "))
            except ValueError:
                print("Entrada inválida! Digite apenas números.")
                continue

            subtotal, produto = calcular_subtotal(opcao, quantidade)
            total += subtotal 
            quant_total+= quantidade
            total_itens_vendidos += quantidade
            print("")
            print(f"Você adicionou {quantidade} unidade(s) de {produto}")
            print(f"Subtotal desta compra R$ {subtotal:.2f}")
            print(f"Valor total acumulado no carrinho R$ {total:.2f}")

            sn = input("Deseja adicionar mais produtos ao carrinho (S/N): ")
        
        print("")
        print(f"Quantidade total de itens no carrinho: {quant_total} unidade(s)")
        print(f"Valor total da compra R$ {total:.2f}")
        exibir_formas_pagamento()

        while True:
            try:
                pag = int(input("Ecolha uma das opções acima: "))
                valor_pago, forma_pagamento = calcular_pagamento(total, pag)
                if valor_pago is None:
                    print("Você escolheu uma forma de pagamento inválida!")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite um número de 1 a 6.")
            
        total_arrecadado_dia += valor_pago

        print("--- Pagamento ---")
        print(f"Forma de pagamento: {forma_pagamento}")
        print(f"Quantidade total de produtos comprados: {quant_total} unidade(s)")
        print(f"Valor total da sua compra R$ {valor_pago:.2f}")

        novo_cliente = input("Deseja atender um novo cliente (S/N): ")

    print("--- Fechamento do dia ---")
    print(f"Total de itens vendidos no dia: {total_itens_vendidos} unidade(s)")
    print(f"Valor total arrecado no dia R$ {total_arrecadado_dia:.2f}")
    print("")