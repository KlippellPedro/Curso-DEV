from produtos import Produtos
def main():
    print("-- Loja de Chocolate Klippel LTDA --\n")
    print("O Chocolate custa R$ 6,00 a unidade")
    print("Caso compre 15 unidades o valor fica R$ 5,00")
    quantidade= int(input("Informe quantos chocolates deseja comprar: "))

    venda= Produtos(quantidade)
    preco_unitario=venda.informar_preco_unitario()
    valor_total = venda.calcular_valor_total()
    #AQUIII
    if valor_total >=100:
        valor_total= valor_total-(valor_total*10/100)
    else:
        valor_total

    print("\n--- Informações da Compra ---\n")
    print(f"Quantidade de chocolates comprados: {quantidade}")
    print(f"Preço unitario do chocolate R$ {preco_unitario}")
    print(f"Valor total R$ {valor_total:.2f}")
    print(f"")

if __name__ == "__main__":
    main()