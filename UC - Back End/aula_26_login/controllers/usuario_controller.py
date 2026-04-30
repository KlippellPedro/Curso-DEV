from database.conexao import Conexao
from werkzeug.security import generate_password_hash, check_password_hash
from utils.token import Token
from utils.gmail_service import GmailService
import re

class UsuarioController:
    def validar(self,nome,email,senha):
        if len(nome) < 3:
            return "Nome invalido!"
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Email invalido!"
        if len(senha) < 6:
            return "Senha deve conter mais de 6 caracteres!"
        return None
    
    def cadastrar(self,nome,email,senha):
        senha_hash = generate_password_hash(senha)
        conn=Conexao.conectar()
        cursor=conn.cursor()
        cursor.execute("""INSERT INTO usuario (nome,email,senha) VALUES (%s,%s,%s)""",(nome,email,senha_hash))
        conn.commit()
        conn.close()
    
    def login(self,email,senha):
        conn=Conexao.conectar()
        cursor=conn.cursor()
        cursor.execute("SELECT nome,senha,admin FROM usuario WHERE email=%s",(email,))
        user=cursor.fetchone()
        conn.close()
        if user and check_password_hash(user[1],senha):
            return {"nome": user[0],"admin": user[2]}
        return None
    
    def listar(self):
        conn=Conexao.conectar()
        cursor=conn.cursor()
        cursor.execute("SELECT nome,email,admin FROM usuario")
        dados=cursor.fetchall()
        conn.close()
        return dados
    
    def gerar_token(self,email):
        token=Token.gerar()
        expira=Token.expirar(10)
        conn=Conexao.conectar()
        cursor=conn.cursor()
        cursor.execute("UPDATE usuario SET token=%s,token_expira=%s WHERE email=%s",(token,expira,email))
        conn.commit()
        conn.close()
        link = f"http://127.0.0.1:5000/redefinir/{token}"
        mensagem = f"""
        <h2>Redefinição</h2>
        <p>Expira em 10 minutos</p>
        <a href="{link}">Redefinir senha</a>
        """
        GmailService.enviar_email(email,"Recuperação",mensagem)
        return token
    
    def validar_token(self,token):
        conn=Conexao.conectar()
        cursor=conn.cursor()
        cursor.execute("SELECT token_expira FROM usuario WHERE token=%s",(token,))
        dado=cursor.fetchone()
        conn.close()
        if not dado:
            return False
        return not Token.expirado(dado[0])
    
    def redefinir_senha(self,token,senha):
        senha_hash = generate_password_hash(senha)
        conn=Conexao.conectar()
        cursor=conn.cursor()
        cursor.execute("UPDATE usuario SET senha=NULL, token=NULL, token_expira=NULL WHERE token=%s",(senha_hash,token))
        conn.commit()
        conn.close()
    