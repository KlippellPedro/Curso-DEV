# Fup para um sistema de vendas
janeiroT = 0.0
fevereiroT = 0.0
marcoT = 0.0
abrilT = 0.0
maioT = 0.0
junhoT = 0.0
op = "s"
while op.lower() == "s":
    vendedores = int(input("Quantas pessoas deseja cadastrar: "))
    for i in range(1, vendedores +1):
        print(f"\n Vendedor: {i}")
        nome = input("Digite o nome do vendedor: ")
        janeiro = float(input("Digite   quanto ele ganhou no mês de janeiro: "))
        fevereiro =  float(input("Digite   quanto ele ganhou no mês de fevereiro: "))
        marco =  float(input("Digite   quanto ele ganhou no mês de março: "))
        abril =  float(input("Digite   quanto ele ganhou no mês de abril: "))
        maio =  float(input("Digite   quanto ele ganhou no mês de maio: "))
        junho =  float(input("Digite   quanto ele ganhou no mês de junho: "))
        janeiroT += janeiro
        fevereiroT += fevereiro
        marcoT += marco
        abrilT += abril
        maioT += maio
        junhoT += junho
        print("")
        print(f"Nome do vendedor: {nome}")
        print(f"Valor arrecadado no mês de janeiro: {janeiro:.2f}")
        print(f"Valor arrecadado no mês de fevereiro: {fevereiro:.2f}")
        print(f"Valor arrecadado no mês de março: {marco:.2f}")
        print(f"Valor arrecadado no mês de abril: {abril:.2f}")
        print(f"Valor arrecadado no mês de maio: {maio:.2f}")
        print(f"Valor arrecadado no mês de junho: {junho:.2f}")
        total = janeiro+fevereiro+marco+abril+maio+junho
        mediames = total/6
        print(f"Media do valor arrecadado nos seis meses: {mediames:.2f}")
        print(f"Total arrecadado nos seis meses: {total:.2f}")
    print("")
    print("Total de vendas entre os vendedores nos seis meses:")
    print("")
    print(f"Janeiro: {janeiroT:.2f}")
    print(f"Fevereiro: {fevereiroT:.2f}")
    print(f"Março: {marcoT:.2f}")
    print(f"Abril: {abrilT:.2f}")
    print(f"Maio: {maioT:.2f}")
    print(f"Junho: {junhoT:.2f}")
    print("")
    op = input("Deseja cadastrar mais vendedores (S/N): ")