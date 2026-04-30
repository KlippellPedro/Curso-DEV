# Importa o uuid (token unico)
import uuid
# Importa o tempo - time
import time
class Token:
    # Gera o token
    @staticmethod
    def gerar():
        return str(uuid.uuid4())
    
    # Define a expiração
    @staticmethod
    def expirar(minuto=10):
        return int(time.time()) + (minuto * 60)
    
    #Verifica se expirou
    @staticmethod
    def expirado(timestamp):
        return time.time() > timestamp