from models.aluno import Aluno
from database.conexao import Conexao

class AlunoController:
    # Método para salvar os dados no banco
    def salvar(self, nome, sobrenome, idade):
        aluno = Aluno()
        aluno.set_nome(nome)
        aluno.set_sobrenome(sobrenome)
        aluno.set_idade(idade)

        conn = Conexao.conectar()
        cursor = conn.cursor()

        sql = """
        INSERT INTO aluno(nome, sobrenome, idade)
        VALUES (?, ?, ?)
        """

        # EXECUTA sql COM DADOS DO OBJETO
        cursor.execute(sql, (
            aluno.get_nome(),
            aluno.get_sobrenome(),
            aluno.get_idade()
        ))

        conn.commit()
        conn.close()