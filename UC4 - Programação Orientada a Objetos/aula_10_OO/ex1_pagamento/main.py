from cliente import Cliente
from menu import Menu
from pagamento import Pagamento

def main():
    print("-- Sistema de Cobrança --\n")
    nome= input("Nome do cliente: ")
    valor= float(input("Valor da compra R$ "))

    # Criar um objeto do cliente
    cliente= Cliente(nome,valor)

    # Exibir o menu de opções
    Menu.exibir_menu()

    # Solicitando e validando a opção escolhida
    opcao= Menu.obter_opcao()

    # Criando o objeto Pagamento e calculando o valor final
    pagamento= Pagamento(valor,opcao)
    valor_final= pagamento.calcular_pagamento()

    # Exibir os resultados
    print("\n","-"*30,"\n")
    cliente.exibir_dados()
    print(f"Vaor total da compra do cliente R$ {valor_final:.2f}")

if __name__ == "__main__":
    main()