from database.conexao import Conexao

from models.usuario import Usuario

from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioController:
    def cadastrar(self, nome, email, senha):

        # Criptografar a senha
        senha_hash = generate_password_hash(senha)
        # Cria objeto usuário
        usuario = Usuario(nome, email, senha_hash)

        conn = Conexao.conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO usuario(nome, email, senha)
                       VALUES(?,?,?)
        """, (usuario.get_nome(), usuario.get_email(), usuario.get_senha())
        )
        conn.commit()
        conn.close()

    def login(self, email, senha):
        conn = Conexao.conectar()
        cursor = conn.cursor()

        # Busca usuário no banco
        cursor.execute("SELECT senha FROM usuario WHERE email = ?", (email,))
        resultado = cursor.fetchone()
        conn.close()

        # Se encontrar o usuário
        if resultado:
            senha_hash = resultado[0]
            # Verifica a senha
            return check_password_hash(senha_hash, senha)
        # Se não encontrar
        return False    
