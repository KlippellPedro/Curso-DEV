# Definindo uma classe chamando cadastro
class Cadastro:
    '''
    Classe responsavel por realizar um cadastro basico de dados de uma pessoa
    '''
    def __init__(self):
        '''
        metodo contrutor da classe cadastro.
        o self representa o proprio objeto, permitindo acessar is atributos 
        e metodos.
        Aqui estamos definindo os atrubitos nome, sobrenome e idade, 
        que inicialmente são vazios ou zero        
        '''
        self.nome = "" # Atributo para armazenar o nome
        self.sobrenome = "" # Atributo para armazenar o sobrenome
        self.idade = 0 # Atributo para armazenar a idade
        self.endereco = ""
        self.bairro = ""
        self.cidade = ""
        self.estado = ""
        self.telefone = ""
        self.email = ""
        self.rg = ""
        self.cpf = ""
        
    def coletar_dados(self): 
        '''
        Metodo para coletar os dados do usuario atraves da função input().
        O dado da idade é convertido para inteiro, pois input retorn string.
        '''
        print("-- Sistema de cadastro tabajaracorp --")
        self.nome = input("Digite o seu nome: ")
        self.sobrenome = input("Digite o seu sobrenome: ")
        self.idade = int(input("Digite a sua idade: "))
        self.endereco = input("Digite o seu endereco: ")
        self.bairro = input("Digite o seu bairro: ")
        self.cidade = input("Digite a sua cidade: ")
        self.estado = input("Digite o seu estado: ")
        self.telefone = input("Digite o seu telefone: ")
        self.email = input("Digite o seu E-mail: ")
        self.rg = input("Digite o seu RG: ")
        self.cpf = input("Digite o seu CPF: ")

    def exibir_dados(self):
        '''
        Metodo para exibir os dados cadastrados no console.
        Mostra as informações utilizando diferentes formas de print.
        '''
        # Forma moderna de exibir dados usando f-string (formação de string)
        print("")
        print(f"Nome completo: {self.nome} {self.sobrenome}")
        print(f"Idade da pesssoa: {self.idade} anos")
        print(f"Endereço completo: {self.endereco}, {self.bairro}, {self.cidade}, {self.estado}")
        print(f"Número de telefone: {self.telefone}")
        print(f"E-mail: {self.email}")
        print(f"RG: {self.rg}")
        print(f"CPF: {self.cpf}")

# Bloco principal - ponto de entrada do programa
if __name__ == "__main__":
    # Criando um objeto da classe cadastro (instancia)
    cadastro = Cadastro()
    # Chamando o metodo para coletar os dados do usuario
    cadastro.coletar_dados()
    # Chamando o metodo para exibir os dados do usuario
    cadastro.exibir_dados()