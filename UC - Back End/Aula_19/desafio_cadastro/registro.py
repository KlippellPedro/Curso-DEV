# Importa função de conexão com o banco
from database import get_connection

class Registro:
    def __init__(self, nome,sobrenome,endereco,numero,comple,bairro,cidade,estado,data_nasc,cpf,rg,email,telefone):
        self.nome = nome
        self.sobrenome=sobrenome
        self.endereco=endereco
        self.numero=numero
        self.comple=comple
        self.bairro=bairro
        self.cidade=cidade
        self.estado=estado
        self.data_nasc=data_nasc
        self.cpf=cpf
        self.rg=rg
        self.telefone = telefone
        self.email = email

    def salvar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO clientes (nome,sobrenome,endereco,numero,complemento,bairro,cidade,estado,data_nasc,cpf,rg,telefone,email)
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
        """, (self.nome,self.sobrenome,self.endereco,self.numero,self.comple,self.bairro,self.cidade,self.estado,self.data_nasc,self.cpf,self.rg,self.telefone,self.email))

        conn.commit()
        conn.close()