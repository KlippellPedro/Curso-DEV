from controllers.sistema import Sistema

if __name__ == "__main__":
    sistema=Sistema()
    novo_cliente= "s"
    while novo_cliente.lower()=="s":
        sistema.processo_compra()
        novo_cliente= input("Deseja atender um novo cliente (S/N): ")

    sistema.fechamento_dia
    print("Obrigado por utilizar o nosso sistema!")