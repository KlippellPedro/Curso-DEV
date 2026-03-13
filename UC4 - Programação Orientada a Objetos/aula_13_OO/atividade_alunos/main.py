from services.sorveteria import Sorveteria
# Ele estava assim tive que adaptar ele para mudar tudo
'''
if __name__ == "__main__": # tava um m ao inves de n no main
    sorveteria = Sorveteria()
    sorveteria.iniciar_compras()
    sorveteria.processar_pagamento()
    sorveteria.finalizar_compra()

'''

def main():
    sorveteria = Sorveteria()
    novo_cliente="s"

    while novo_cliente.lower()=="s":
        sorveteria.iniciar_compras()
        sorveteria.processar_pagamento()
        sorveteria.finalizar_compra()
        novo_cliente=input("\nDeseja atender um novo cliente (S/N): ")
        if novo_cliente.lower()=="s":
            sorveteria.pedidos=[]
            continue
        else:
            break
        
    sorveteria.fechar_caixa()

if __name__=="__main__":
    main()
