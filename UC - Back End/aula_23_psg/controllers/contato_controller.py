from database.conexao import BancoDados

# Salvar dados no banco de dados
class ContatoController:
    def salvar(self, contato):
        conn = BancoDados.conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO fale_conosco
                    (nome,sobrenome,datanasc,endereco,bairro,cidade,estado,
                    sexo,telefone,email,usuario,senha,observacao)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            contato._nome,
            contato._sobrenome,
            contato._datanasc,
            contato._endereco,
            contato._bairro,
            contato._cidade,
            contato._estado,
            contato._sexo,
            contato._telefone,
            contato._email,
            contato._usuario,
            contato._senha,
            contato._observacao
        )
        )
        conn.commit()
        conn.close()