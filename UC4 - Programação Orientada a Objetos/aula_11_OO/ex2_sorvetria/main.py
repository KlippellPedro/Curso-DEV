from services.sorveteria import Sorveteria

if __name__== "__main__":
    sorveteria=Sorveteria()
    sorveteria.iniciar_compras()
    sorveteria.processar_pagamento()
    sorveteria.finalizar_compra()