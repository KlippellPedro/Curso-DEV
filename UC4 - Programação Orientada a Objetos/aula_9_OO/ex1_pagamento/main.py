from cliente import Cliente
from pagamento import Pagamento

def main():
    print("-- Sistema de Controle de Pagamento --\n")
    nome=input("Informe o nome do cliente: ")
    valor= float(input("Informe o valor da compra R$ "))

    # Exibir o menu de opções
    print("\n--- Menu de Forma de Pagamento ---\n")
    print("1- Á vista em Diheiro ou Pix - 10% de desconto")
    print("2- Á prazo 30 dias - 5% de desconto")
    print("3- Á prazo 60 dias - sem desconto ou acréscimo")
    print("4- Á prazo 90 dias - 5% de acréscimo")
    print("5- No cartão de débito - 8% de desconto")
    print("6- No caderno fiado - 7% de desconto")

    # Validação da opção
    while True:
        try:
            opcao= int(input("Escolha uma opção (1 a 6): "))
            if 1<= opcao <=6:
                break
            else:
                print("Opção inválida! Escolha um número de 1 a 6")
        except ValueError:
            print("Entrada Inválida!")
    
    # Criar objetos das classes
    cliente= Cliente(nome,valor)
    pagamento=Pagamento(cliente)

    # Receber o calculo do pagamento
    valor_final=pagamento.calcular_pagamento(opcao)

    # Exibir os resultados
    print("\n","-"*30,"\n")
    print(f"Nome do cliente: {cliente.nome}")
    print(f"Valor total da compra R$ {valor_final:.2f}")
if __name__=="__main__":
    main()