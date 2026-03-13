from produtos import Produtos

def main():
    print("-- Mercado Klippel LTDA --\n")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Informe o preço do produto R$ "))
    quantidade= int(input("Informe a quantidade que deseja comprar: "))

    venda= Produtos(quantidade,preco,nome)

    valor_total = venda.calcular_valor_total()

    print("\n--- Informações da Compra ---\n")
    print(f"Produto comprado: {nome}")
    print(f"Preço unitário R$ {preco:.2f}")
    print(f"Quantidade de produtos comprados: {quantidade}")
    print(f"Valor total R$ {valor_total:.2f}")

if __name__ == "__main__":
    main()