# Sistema para aparecer na tela do número 1 até o número que foi digitado, ao final ele vai mostrar a quantidade de numeros impressos
valor = int(input("Informe um número inteiro: "))
#Iniciar a variável soma com um valor
soma = 0
# Estrutura de repetição for
for i in range(1, valor +1):
    soma = soma+1
    # soma +=1
    print("Valor da variavel i: ",i)
# Exibir o total de vezes que a variável i foi impressa
print("")
print("Quantidade de números impressos: ",soma)