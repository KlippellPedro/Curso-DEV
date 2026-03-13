from controllers.sistema import Sistema

def main():
    sistema= Sistema()
    # Controle para atender varios clientes sem precisar reiniciar o programa
    novo_cliente="s"
    while novo_cliente.lower() == "s":
        sistema.processo_compra()
        novo_cliente= input("Deseja atender um novo cliente (S/N): ")

    sistema.fechamento_dia()
    print("Obrigado por deixar a minha empresa mais rica")

if __name__ == "__main__":
    main()