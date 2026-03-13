def obter_opcao():
    while True:
        try:
            opcao = int(input("Selecione uma das opções: "))
            if 1<= opcao <= 5:
                return opcao # Retorna se a opção for válida
            else:
                print("Opção inválida! Escolha um número entre 1 e 5.")
        
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

def obter_quantidade():
    while True:
        try:
            quantidade = int(input("Quantos picolés deseja comprar: "))
            if quantidade > 0:
                return quantidade # Retorna se a quantidade for valida
            else:
                print("Quantidade deve ser maior que zero.")

        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

def calcular_subtotal(opcao, quantidade):
    precos = {1: 1.00, 2: 1.25,3: 1.50,4: 1.80,5: 2.00}
    sabores = {1: "Uva", 2: "Laranja",3: "Milho",4: "Coco Queimado",5: "Tamarindo"}
    preco_unitario = precos[opcao]
    subtotal = quantidade * preco_unitario
    sabor = sabores[opcao]
    return subtotal, sabor

def deseja_continuar():
    while True:
        resposta = input("Deseja continuar comprando (S/N): ").strip().lower()
        if resposta in ["s", "n"]:
            return resposta == "s" # Retorna True para "s" e False para "n"
        else:
            print("Responda com 'S' para sim ou 'N' para não.")