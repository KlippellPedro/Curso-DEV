class Loja_de_vendas():
    def __init__(self, valor):
        self.valor = valor
        self.quant = quant
    
    def desconto(self,percentual):
        return self.valor-(self.valor*percentual)
    
    def calculo(self):
        return self.valor*self.quant

if __name__ == "__main__":
    print("-- Loja e Vendas GR!TTA --")
    valor = float(input("\nDigite o valor do produto: "))
    quant = int(input(f"Quantas unidades deseja comprar: "))

    print("\n","-"*40,"\n")
    
    calc = Loja_de_vendas(valor)
    if quant >=3:
        print(f"Valor total sem desconto R$ {valor}")
        print(f"Valor do desconto R$ {valor*0.05}")
        print(f"Valor com 5% de desconto R$ {calc.desconto(0.05)}")
        print(f"Quantidade de produtos comprados: {quant}")
    elif quant == 2 or 1:
        print(f"Valor total da comra R$ {valor}")
        print(f"Quantidade de produtos: {quant}")
        print(f"\nPara obter desconto é preciso comprar 3 produtos")
    else:
        print("Por favor digite um número válido")
        print("Tente Novamente!")