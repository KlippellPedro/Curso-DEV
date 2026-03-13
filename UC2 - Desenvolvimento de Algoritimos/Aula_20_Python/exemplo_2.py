# Sistema para realizar compras de picolés usando função
# Exibe o menu com os sabores e preços disponiveis
def exibir_menu():
    print("-- Sorveteria --")
    print("")
    print("--- Menu de sabores dos picolés ---")
    print("1- Picolé de Uva R$ 1,00")
    print("2- Picolé de Laranja R$ 1,25")
    print("3- Picolé de Milho R$ 1,50")
    print("4- Picolé de Coco queimado R$ 1,80")
    print("5- Picolé de Tamarindo R$ 2,00")

# Solicitar ao usuario uma opção de picoles valida(1 a 5)
def obter_opcao():
    while True:
        try:
            opcao = int(input("Selecione uma das opções (1 a 5): "))
            if 1<= opcao <=5:
                return opcao # Retorna se a opção for valida
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")
def obter_quantidade():
    while True:
        try:
            quantidade = int(input("Quantos picolés deseja comprar? "))
            if quantidade > 0:
                return quantidade
            else:
                print("A quantidade deve ser maior que zero")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")
# Calcula o subtotal da compra e retorna o nome do sabor
def calcular_subtotal(opcao, quantidade):
    # Dicionário com prelos dos picolés
    preco = {1: 1.00, 2: 1.25, 3: 1.50, 4: 1.80 ,5: 2.00}
    # Dicionário com nomes dos sabores
    sabores = {1: "Uva", 2: "Laranja", 3: "Milho", 4: "Coco queimado", 5: "Tamarindo"}
    preco_unitario = preco[opcao] # Busca o preço conforme a opção
    subtotal = quantidade * preco_unitario # Calcula o valor total
    sabor = sabores[opcao] # Busca o nome do sabor
    return subtotal, sabor # Retorna ambos

# Pergunta ao usuario se deseja continuar comprando
def deseja_continuar():
    while True:
        resposta = input("Deseja continuar comprando (S/N): ").strip().lower()
        if resposta in ["s", "n"]:
            return resposta == "s" # Retorna True para "s" e False para "n"
        else:
            print("Responda com 'S' para sim ou 'N' para não.")

# Função principal que processa toda compra
def processar_compra():
    total = 0.0
    quanttotal = 0
    continuar = True # Controle do loop principal

# Loop principal da compra
    while continuar:
        exibir_menu() # Exibi o menu de picoles
        opcao = obter_opcao() # Obtem a escolha do sabor
        quantidade = obter_quantidade() # Obtem a quantidade desejada
        subtotal, sabor = calcular_subtotal(opcao, quantidade) # Calcula o subtotal

        # Exibe os detalhes da compra atual
        print(f"Você comprou {quantidade} unidade(s) do picolé {sabor}")
        print(f"Subtotal da compra até o momento R$ {subtotal:.2f}")
        
        # Atualizar o total geral e a quantidade
        total += subtotal
        quanttotal += quantidade

        # Mostra o valor acumulado
        print(f"Total acumulado R$ {total:.2f}")
        print("")

        #Verificar se o cliente deseja continuar
        continuar = deseja_continuar()

        # Exibe o resumo final da compra
        print("")
        print(f"Quantidade total de picolés comprados: {quanttotal} unidades.")
        print(f"Valor total da sua compra R$ {total}")
        print("Obrigado pela sua compra!!")

# Inicio da execução do programa
processar_compra()