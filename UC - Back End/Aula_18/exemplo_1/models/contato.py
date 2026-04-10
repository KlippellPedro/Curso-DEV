# Importa função de conexão com o banco
from database import get_connection

class Contato:
    # Método construtor
    def __init__(self, nome, email, telefone, data_nascimento):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    # Método para salvar no banco
    def salvar(self):
        # Conecta ao banco
        conn = get_connection()
        # Cria cursor
        cursor = conn.cursor()
        # Executa o comando INSERT usando parâmetros
        cursor.execute("""
            INSERT INTO contato (nome, email, telefone, dataNascimento)
                       VALUES(?, ?, ?, ?)
        """, (self.nome, self.email, self.telefone, self.data_nascimento))

        # Confirma alteração
        conn.commit()
        # Fecha conexão
        conn.close()    
        