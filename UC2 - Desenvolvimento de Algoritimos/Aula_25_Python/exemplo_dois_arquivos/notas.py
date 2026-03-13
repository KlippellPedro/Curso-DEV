# Objetivo desse arquivo é realizar a média das notas digitadas
def media(nota1, nota2, nota3, nota4):
    resultado = (nota1+nota2+nota3+nota4)/4
    return resultado

def situacao(curriculo_media):
    if curriculo_media >= 7:
        return "Aprovado"
    elif curriculo_media >=5:
        return "Recuperação"
    else:
        return "Reprovado"
    