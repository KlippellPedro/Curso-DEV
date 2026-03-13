def calcular_subtotal(opcao,quantidade):
    if opcao == 1:
        return quantidade * 5.00, "Arroz (1Kg)"
    elif opcao == 2:
        return quantidade * 7.50, "Feijão (1Kg)"
    elif opcao == 3:
        return quantidade * 4.00, "Leite (1L)"
    elif opcao == 4:
        return quantidade * 30.00, "Café (500g)"
    else:
        return 0, "Opção inválida"
    
def calcular_pagamento(total,pag):
    if pag == 1:
        return total * 0.90, "A vista em dinheiro ou PIX - 10% de desconto"
    elif pag == 2:
        return total * 0.95, "Cartão de débito - 5% de desconto"
    elif pag == 3:
        return total, "Cartão de crédito 30 dias - mesmo valor"
    elif pag == 4:
        return total *1.05, "Cartão de crédito em 2X - acréscimo de 5%" 
    elif pag == 5:
        return total *1.10, "Cartão de crédito em 3X - acréscimo de 10%" 
    elif pag == 6:
        return total *1.15, "Cartão de crédito em 4X - acréscimo de 15%" 
    else:
        return None, "Opção inválida!"