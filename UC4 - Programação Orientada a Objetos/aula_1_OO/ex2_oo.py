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
        
    def coletar_dados(self): 
        '''
        Metodo para coletar os dados do usuario atraves da função input().
        O dado da idade é convertido para inteiro, pois input retorn string.
        '''
        print("-- Sistema de cadastro tabajaracorp --")
        self.nome = input("Digite o seu nome: ")
        self.sobrenome = input("Digite o seu sobrenome: ")
        self.idade = int(input("Digite a sua idade: "))

    def exibir_dados(self):
        '''
        Metodo para exibir os dados cadastrados no console.
        Mostra as informações utilizando diferentes formas de print.
        '''
        # Forma moderna de exibir dados usando f-string (formação de string)
        print("")
        print(f"Nome completo: {self.nome} {self.sobrenome}")
        print(f"Idade da pesssoa: {self.idade} anos")

        # Forma tradicional de exibir dados, separando por virgula
        print("Nome completo: ", self.nome, self.sobrenome)
        print("Idade: ",self.idade, "anos")

# Bloco principal - ponto de entrada do programa
if __name__ == "__main__":
    # Criando um objeto da classe cadastro (instancia)
    cadastro = Cadastro()
    # Chamando o metodo para coletar os dados do usuario
    cadastro.coletar_dados()
    # Chamando o metodo para exibir os dados do usuario
    cadastro.exibir_dados()