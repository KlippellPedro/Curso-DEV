class Usuario:
    def __init__(self, nome, email, senha, admin=0):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.admin = admin
    
    def get_nome(self):
        return self.nome
    
    def get_email(self):
        return self.email
    
    def get_senha(self):
        return self.senha
    
    def get_admin(self):
        return self.admin
    
    def set_nome(self, nome):
        self.nome = nome
    
    def set_email(self, email):
        self.email = email
    
    def set_senha(self, senha):
        self.senha = senha
    
    def set_admin(self, admin):
        self.admin = admin
        
    