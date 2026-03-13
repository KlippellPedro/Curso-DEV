# Sistema para aparecer na tela do número 1 até o número que foi digitado
valor = int(input("Informe um número inteiro: "))
# Utilizando o (for)
for i in range(1, valor +1):
    print("Valor da variavel 1: ",i)
# O range(1, valor +1) significa para 1 de 1 até o valor da variável, pois o range em python vai até o valor final.
# Como seria no java: 
# for (int i = 1; i < valor; i++)