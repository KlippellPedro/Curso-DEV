# 
from menu import exibir_menu
from compras import obter_opcao, obter_quantidade, calcular_subtotal, deseja_continuar

def processar_compra():
    total = 0.0
    quantidade = 0
    quanttotal = 0
    continuar = True

    while continuar:
        exibir_menu() # Exibe o cardépio
        opcao = obter_opcao() # Obtém a escolha do sabor
        quantidade = obter_quantidade() # Obtém a quantidade desejada
        subtotal, sabor = calcular_subtotal(opcao, quantidade) # Calcula o subtotal

        print(f"\nVocê comprou {quantidade} unidade(s) do picolé de {sabor}")
        print(f"\nSubtotal da compra R$ {subtotal:.2f}")

        total += subtotal
        quanttotal += quantidade

        print(f"\nTotal acumulado R$ {total:.2f}")
        print("")

        continuar = deseja_continuar()

    print("")
    print(f"Quantidade total de picolés comprados: {quantidade} unidade(s).")
    print(f"Valor total da sua compra R$ {total:.2f}")
    print("\nObrigado por comprar na sorveteria Guaxilandia")

if __name__ == "__main__":
    processar_compra()