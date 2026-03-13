from pagamento import Pagamento
def main():
    print("-- Pagamentos Klippel LTDA --")
    nome= input("\nDigite o nome do produto: ")
    valor= float(input("Digite o valor do produto: "))
    quantidade= int(input("Digite a quantidade que deseja comprar: "))
    print("\n--- Opção de Pagamento ---\n")
    print("1- Á vista em dinheiro ou pix - 15% de desconto")
    print("2- Á vista no cartão de débito - 10% de desconto")
    print("3- Parcelado em 2X - Preço normal")
    print("4- Parcelado em 3X - 10% de acréscimo")
    opcao= int(input("Opção de pagamento: "))

    pagamentos= Pagamento(nome,valor,quantidade,opcao)
    opcao= pagamentos.opcao_pagamento()
    valor_total= pagamentos.valor_pagamento()

    print("\n--- Informações da Compra ---\n")
    print(f"Nome do produto: {nome}")
    print(f"Quantidade comprada: {quantidade}")
    print(f"Valor total da compra: {valor_total*quantidade:.2f}")
    print(f"Opção de pagamento: {opcao}")


if __name__ == "__main__":
    main()