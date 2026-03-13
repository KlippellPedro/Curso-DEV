from controllers.mercado_controller import MercadoController

def main():
    mercado=MercadoController()
    novo_cliente="s"

    while novo_cliente.lower()=="s":
        mercado.atender_cliente()
        novo_cliente=input("Deseja atender um novo cliente (S/N): ")
        
    mercado.fechar_caixa()

if __name__=="__main__":
    main()