from database.conexao import DataBase

class ContatoController:
    def salvar(self,contato):
        conn=DataBase.get_connection()
        cursor=conn.cursor()
    
        cursor.execute("""INSERT INTO fale_conosco (nome,sobrenome,data_nascimento,bairro,endereco,cidade,estado,sexo,telefone,email,usuario,senha,observacao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (contato._nome,contato._sobrenome,contato._data_nascimento,contato._bairro,contato._endereco,
                        contato._cidade,contato._estado,contato._sexo,contato._telefone,contato._email,
                        contato._usuario,contato._senha,contato._observacao))
        conn.commit()
        cursor.close()
        conn.close()