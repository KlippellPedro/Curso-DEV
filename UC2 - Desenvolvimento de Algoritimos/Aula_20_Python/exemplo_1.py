# Sistema para calcular a comissão de corretor de imoveis
def obter_dados_corrretor():
    # Solicita o nome do corretor e o valor do imovel vendido
    print("-- Empresa de venda de imôveis --")
    nome = input("Digite o nome do corretor: ")
    while True:
        try:
            venda = float(input("Digite o valor do imôvel que ele vendeu: "))
            if venda < 0:
                print("O valor da venda não pode ser negativo.")
                print("Tente novamente!")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um valor numérico")
    return nome, venda
def calcular_comissao(valor_venda):
    # Calcular a comissão com base no valor do imovel vendido
    if valor_venda >= 50000:
        return valor_venda*0.20
    elif valor_venda >= 30000:
        return valor_venda*0.15
    else:
        return valor_venda*0.10
def exibir_resultado(nome, comissao):
    # Exibe o nome e o valor da comissão
    print("")
    print("-- Informações do corretor --")
    print(f"Nome do corretor: {nome}")
    print(f"Valor total da comissão da venda R$ {comissao}")
    print("")

def main():
    # Função principal que controla o fluxo do programa
    while True:
        nome, valor_venda = obter_dados_corrretor
        comissao = calcular_comissao(valor_venda)
        exibir_resultado(nome, comissao)
        continuar = input("Deseja continuar pesquisando (S/N): ").lower()
        if continuar != "s":
            print("Programa encerrado!")
            break

# Execução do programa
if __name__ == "__main__":
    main()