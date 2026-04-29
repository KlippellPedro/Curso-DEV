import sqlite3
class BancoDados:
    database = "database.db"

    # Método para conectar ao banco
    @classmethod
    def conectar(cls):
        #criar conexão com o banco
        conn = sqlite3.connect(cls.database)
        # Permite acessar colunas pelo nome
        conn.row_factory = sqlite3.Row
        # Retorna conexão
        return conn

    # Cria tabela se não existir
    @classmethod
    def criar_tabela(cls):
        # Conecta ao banco
        conn = cls.conectar()
        # Cria um cursor
        cursor = conn.cursor()

        # Executa o código SQL para criar a tabela
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fale_conosco(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    sobrenome TEXT,
                    datanasc TEXT,
                    endereco TEXT,
                    bairro TEXT,
                    cidade TEXT,
                    estado TEXT,
                    sexo TEXT,
                    telefone TEXT,
                    email TEXT,
                    usuario TEXT,
                    senha TEXT,
                    observacao TEXT
                    )
        """) 
        # Salva alterações
        conn.commit()
        # Fecha conexão
        conn.close()   