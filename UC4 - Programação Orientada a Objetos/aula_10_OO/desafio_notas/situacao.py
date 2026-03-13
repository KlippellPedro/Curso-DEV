class Situacao:
    @staticmethod
    def calcular_situacao(media_final):
        if media_final >= 7:
            return("Aprovado")
        elif media_final >= 5:
            return("Recuperação")
        else:
            return("Reprovado")