from produto import Produto
from pagamento import Pagamento

def main():
    print("-- Loja Klippel LTDA --\n")
    nome= input("Digite o nome do produto: ")
    preco= float(input("Digite o valor do produto R$ "))
    quantidade= int(input("Digite a quantidade que deseja comprar: "))

    print("\n--- Menu de Forma de Pagamento ---\n")
    print("1 - Á vista em dinheiro ou PIX, 15% de desconto.")
    print("2 - Á vista no cartão de débito, 10% de desconto")
    print("3 - Parcelado em 2X, preço normal sem juros.")
    print("4 - Parcelado em 4X, com  acréscimo de 10%.\n")
    opcao= int(input("Escolha uma das opções (1 a 4): "))
    print("\n","-"*30,"\n")

    # Criar um objeto Produto com os dados fornecidos
    produto = Produto(nome,preco,quantidade)
    # Criar um objeto Pagamento, passando o produto e a opção escolhida
    pagamento = Pagamento(produto,opcao)

    # Verificar se o pagamento é válido
    if 1 <= opcao <= 4:
        total= pagamento.calcular()

        # Exibir as informações da compra
        print(f"Nome do produto: {produto.nome}")
        print(f"Quantidade de produtos comprados: {produto.quantidade}")
        print(pagamento.mensagem)

        # Se o pagamento for parcelado, mostra o valor da parcela
        if pagamento.parcelas is not None:
            parcela_valor=total / pagamento.parcelas
            print(f"Produto parcelado em {pagamento.parcelas}X de R$ {parcela_valor:.2f}")
        print(f"Valor total da compra R$ {total:.2f}")
    else:
        print("Você escolheu uma opção inválida!")

if __name__ == "__main__":
    main()