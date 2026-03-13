class LojaEletronico:
    def __init__(self,nome_produto,preco_fabrica,percentual_imposto,percentual_revendedor):
        self.nome_produto = nome_produto
        self.preco_fabrica = preco_fabrica
        self.percentual_imposto = percentual_imposto
        self.percentual_revendedor = percentual_revendedor
    
    def calcular_imposto(self):
        return self.preco_fabrica* self.percentual_imposto
    
    def calcular_lucro_revendedor(self):
        return self.preco_fabrica * self.percentual_revendedor
    
    def calcular_preco_final(self):
        return self.preco_fabrica+self.calcular_imposto()+self.calcular_lucro_revendedor()

if  __name__ == "__main__":
    print("-- Loja de veículos Klippel LTDA --")
    nome = input("Informe o nome do produto: ")
    preco_fabrica = float(input("Digite o valor do produto na fábrica R$ "))
    percentual_imposto = float(input("Digite o percentual do imposto % "))
    percentual_revendedor = float(input("Digite o percentual do revendedor % "))
    garantia = float(input("Qual o valor da garantia R$ "))

    produto = LojaEletronico(nome,preco_fabrica,percentual_imposto,percentual_revendedor)
    imposto = produto.calcular_imposto()
    lucro = produto.calcular_lucro_revendedor()
    preco_final = produto.calcular_preco_final()

    print("")
    print(f"Nome do produto: {produto.nome_produto}")
    print(f"Valor do produto na fabrica R$ {produto.preco_fabrica:.2f}")
    print(f"Valor do imposto cobrado do produto R$ {imposto:.2f}")
    print(f"Percentual do imposto cobrado % {percentual_imposto}")
    print(f"Valor do lucro do revendedor R$ {lucro:.2f}")
    print(f"Percentual do de lucro do revendedor % {percentual_revendedor}")
    print(f"Valor final do produto para revenda R$ {preco_final:.2f}")
    print(f"Valor da garantia R$ {garantia}")