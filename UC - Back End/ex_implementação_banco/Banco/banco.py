# pip install mysql-connector-python
# Mudar para a versão 3.
import mysql.connector

class preenchendoBanco():

    def __init__(self):
        self.host="localhost",
        self.user="root",
        self.password=""
        self.database="banco_teste"
        
        self.cnx=mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor= self.cnx.cursor()

    def criar_perfis(self):
        perfis= ("Administrador", "Usuario")
        for perfil in perfis:
            self.cursor.execute("INSERT INTO perfis (nome_perfil) VALUES (%s)", (perfil,))
            self.cnx.commit()