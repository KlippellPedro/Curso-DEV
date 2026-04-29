class Aluno:
    def __init__(self, nome=None, sobrenome=None, idade=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def get_nome(self):
        return self.nome
    def get_sobrenome(self):
        return self.sobrenome
    def get_idade(self):
        return self.idade

    def set_nome(self, nome):
        self.nome = nome
    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome
    def set_idade(self, idade):
        self.idade = idade            