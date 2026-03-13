from trakinas import VendaTrakinas

def main():
    print("-- Mercado Klippel LTDA --\n")
    print("Preço da trakina R$ 4,50 a unidade")
    print("Comprando 20 unidades ou mais, você vai pagar R$ 4,00 a unidade")
    quantidade= int(input("Informe a quantidade de trakinas que deseja comprar: "))

    venda= VendaTrakinas(quantidade)

    valor_total = venda.calcular_valor_total()
    preco_unitario=venda.informar_preco_unitario()

    print("\n--- Informações da Compra ---\n")
    print(f"Quantidade de trakinas compradas: {quantidade}")
    print(f"Você vai pagar R$ {preco_unitario:.2f} a unidade")
    print(f"Valor total da compra: {valor_total:.2f}")

if __name__ == "__main__":
    main()