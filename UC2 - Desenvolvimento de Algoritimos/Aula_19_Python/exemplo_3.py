# Função para calcular a media das notas
def media(nota1, nota2, nota3, nota4):
    resultado = (nota1+ nota2+ nota3+ nota4)/4
    return(resultado)

def main():
    print("-- Sistema escolar utilizando função --")
    n1 = int(input("Digite a primeira nota: "))
    n2 = int(input("Digite a segunda nota: "))
    n3 = int(input("Digite a terceira nota: "))
    n4 = int(input("Digite a quarta nota: "))

    resultado = media(n1, n2, n3, n4)

    print("")
    print(f"Média final: {resultado:.2f}")

if __name__ == "__main__":
    main()