import sqlite3
# Função para conectar ao banco
def get_connection():
    # Conecta ao banco agenda.db ou cria se não existir
    conn = sqlite3.connect("agenda.db")
    # Permite acessar colunas pelo nome
    conn.row_factory = sqlite3.Row
    # Retorna a conexão
    return conn

# Função para criar tabela automaticamente
def init_db():
    # Cria conexão
    conn = get_connection()
    # Cria cursor para executar os comandos SQL
    cursor = conn.cursor()
    # Executa o comando SQL para criar a tabela se não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contato(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   telefone TEXT NOT NULL,
                   dataNascimento TEXT NOT NULL
                   )
    """)
    # Salva alterações
    conn.commit()
    # Fecha conexão
    conn.close()