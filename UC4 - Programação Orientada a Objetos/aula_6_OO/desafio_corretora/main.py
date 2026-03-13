from dados import Corretora
def main():
    print("-- Corretora Klippel LTDA --")
    nome= input("Digite o nome do vendedor: ")
    valor_imovel= float(input("Digite o valor do imovel: "))

    corretor= Corretora(nome,valor_imovel)
    comissao= corretor.calculo_comissao()
    print("")
    print(f"Nome do vendedor: {corretor.nome}")
    print(f"Valor do imovel: {corretor.valor_imovel}")
    print(f"Valor da comissão: {comissao:.2f}")

if __name__ == "__main__":
    main()