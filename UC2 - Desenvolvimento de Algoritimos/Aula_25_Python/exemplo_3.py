from datetime import datetime

def exibir_menu_picoles():
    print("## Sorveteria TabajaraCorp ##")
    print("-- Menu de sabores --")
    print("1 - Picolé de Uva R$ 1,00")
    print("2 - Picolé de Laranja R$ 1,25")
    print("3 - Picolé de Milho R$ 1,50")
    print("4 - Picolé de Coco queimado R$ 1,80")
    print("5 - Picolé de Tamarindo R$ 2,00")

def obter_preco_sabor(opcao):
    sabores = {
        1: ("Uva", 1.00),
        2: ("Laranja", 1.25),
        3: ("Milho", 1.50),
        4: ("Coco queimado", 1.80),
        5: ("Tamarindo: ", 2.00)
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
            lista_compras.append((nome_picole, quantidade, subtotal))

            print(f"Você comprou {quantidade} unidade(s) do picolé de {nome_picole}")
            print(f"Subtotal R$ {subtotal:.2f}")
            print(f"Total acumulado R$ {total:.2f}")
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
            continue

        continuar = input("Deseja continuar comprando (S/N): ")

    return total, quantidade_total, lista_compras

def exibir_menu_pagamento():
    print("\n## Menu de forma de pagamento ##")
    print("1 - A vista em dinheiro ou PIX, 10% de desconto")
    print("2 - Cartão de débito, 5% de desconto")
    print("3 - Cartão de crédito 30 dias, mesmo valor") 
    print("4 - Cartão de crédito em 2X, acréscimo de 5%")
    print("5 - Cartão de crédito em 3X, acréscimo de 10%") 
    print("6 - Cartão de crédito em 4X, acréscimo de 15%")
    
def aplicar_pagamento(total):
    forma_pagamento = ""
    while True:
        try:
            exibir_menu_pagamento()
            opcao =int(input("Escolha uma opção de pagamento: "))

            if opcao == 1:
                desconto = total * 0.10
                total -= desconto
                forma_pagamento = "Dinheiro ou PIX - 10% de desconto"
                print(f"Desconto de 10% aplicado R$ {desconto:.2f}")
            elif opcao == 2:
                desconto = total * 0.05
                total -= desconto
                forma_pagamento = "Cartão de débito - 5% de desconto"
                print(f"Desconto de 5% aplicado R$ {desconto:.2f}")
            elif opcao == 3:
                forma_pagamento = "Cartão de crédito 30 dias, mesmo valor"
                print("Pagamento sem desconto ou acréscimo")
            elif opcao == 4:
                acrescimo = total * 0.05
                total += acrescimo
                forma_pagamento = "Cartão de crédito 2X - 5% de acréscimo"
                print(f"Acréscimo de 5% aplicado R$ {acrescimo:.2f}")
                print(f"Parcelado em 2X de R$ {total / 2:.2f}")
            elif opcao == 5:
                acrescimo = total * 0.10
                total += acrescimo
                forma_pagamento = "Cartão de crédito em 3X - 10% de acréscimo"
                print(F"Acréscimo de 10% aplicado R$ {acrescimo:.2f}")
                print(f"Parcelado em 3X de R$ {total / 3:.2f}")
            elif opcao == 6:
                acrescimo = total * 0.15
                total += acrescimo
                forma_pagamento = "Cartão de crédito em 4X - 15% de acréscimo"
                print(f"Acréscimo de 15% aplicado R$ {acrescimo:.2f}")
                print(f"Parcelado em 4X de R$ {total / 4:.2f}")
            else:
                print("Opção inválida. Tente novamente.")
                continue

            break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

    return total, forma_pagamento

def gerar_relatorio(lista_compras, total_final, quantidade_total, forma_pagamento):
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nome_arquivo = input("Informe o nome do arquivo (ex: nome.txt): ")
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        f.write("### Relatório de compras - Sorveteria TabajaraCorp ###\n")
        f.write(f"Data e hora: {data_atual}\n\n")
        f.write("Itens comprados:\n")
        for nome, qtd, subt in lista_compras:
            f.write(f" - {qtd}x {nome} | Subtotal: R$ {subt:.2f}")
        f.write("\n")   
        f.write(f"Total de picolés comprados: {quantidade_total} unidade(s)\n")
        f.write(f"Forma de pagamento: {forma_pagamento}\n") 
        f.write(f"Valor final da compra R$ {total_final:.2f}\n")
        f.write("\nObrigado por compra na Sorveteria TabajaraCorp.")

def main():
    total, quantidade_total, lista_compras = realizar_compra()
    print(f"Quantidade total de picolés comprados: {quantidade_total} unidade(s).")
    total_final, forma_pagamento = aplicar_pagamento(total)
    print(f"\nValor total da compra R$ {total_final:.2f}")
    gerar_relatorio(lista_compras, total_final, quantidade_total, forma_pagamento)
    print("\nRelatório gerado com sucesso!")

if __name__ == "__main__":
    main()    
