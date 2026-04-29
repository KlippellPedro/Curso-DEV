class Contato:
    # Construtor da classe
    def __init__(self):
        
        self._nome = ""
        self._sobrenome = ""
        self._datanasc = ""
        self._endereco = ""
        self._bairro = ""
        self._cidade = ""
        self._estado = ""
        self._sexo = ""
        self._telefone = ""
        self._email = ""
        self._usuario = ""
        self._senha = ""
        self._observacao = ""

    def set_nome(self, valor):
        self._nome = valor

    def set_sobrenome(self, valor):
        self._sobrenome = valor 

    def set_datanasc(self, valor):
        self._datanasc = valor

    def set_endereco(self, valor):
        self._endereco = valor

    def set_bairro(self, valor):
        self._bairro = valor

    def set_cidade(self, valor):
        self._cidade = valor

    def set_estado(self, valor):
        self._estado = valor

    def set_sexo(self, valor):
        self._sexo = valor

    def set_telefone(self, valor):
        self._telefone = valor

    def set_email(self, valor):
        self._email = valor

    def set_usuario(self, valor):
        self._usuario = valor

    def set_senha(self, valor):
        self._senha = valor

    def set_observacao(self, valor):
        self._observacao = valor

    # Getters
    def get_nome(self):
        return self._nome 
    def get_sobrenome(self):
        return self._sobrenome 
    def get_datanasc(self):
        return self._datanasc
    def get_endereco(self):
        return self._endereco
    def get_bairro(self):
        return self._bairro
    def get_cidade(self):
        return self._cidade
    def get_estado(self):
        return self._estado
    def get_sexo(self):
        return self._sexo
    def get_telefone(self):
        return self._telefone
    def get_email(self):
        return self._email
    def get_usuario(self):
        return self._usuario
    def get_senha(self):
        return self._senha
    def get_observacao(self):
        return self._observacao                                                             
