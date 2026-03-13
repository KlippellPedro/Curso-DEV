# Comentário de uma única linha
'''
Comentário 
para várias linhas com apóstrofe
'''
"""
Comentário 
para várias linhas com aspas
"""
# Criando uma classe com o nome Mensagem
class Mensagem:
    '''
    Classe que representa uma mensagem a ser exibida no console.
    Contém metodos para exibir mensagens simples, com quebra de linha, 
    e controlando o comportamento do print
    '''
    def __init__(self):
        '''
        Método contrutor da classe.
        O paramentro self representa a propria instancia (objeto) que
        esta sendo criado.
        self é uma convenção no python e é usado para acessar os atributos
        e metodos do objeto.
        '''   
        pass # No momento, não há atributos a serem inicializados

    def mensagem_inicial(self):
        '''
        Metodo para eibir uma mensagem inicial no console.
        O self permite que o metodo seja chamado pelo objeto da classe.
        '''
        print("Hello World")
        print("Que emoção, meu primero código em python, orientado a objetos.")
    
    def mensagem_sem_quebra(self):
        '''
        Metodo para exibir duas mensagens na mesma linha utilizando o
        parametro end.
        por padrão, o print adiciona uma quebra de linah ao final, mas 
        ao usar o end="", evitamos a quebra de linha.
        self permite que este metodo pertença ao objeto criado.
        '''
        print("Utilizando o end para manter o texto na mesma linha", end="")
        print(" - Aqui temos a continuação do texto.")

    def mensagem_com_quebra(self):
        '''
        Metodo para exibir mensagens utilizando o caracter especial \n 
        que força a quebra de linha no ponto desejado.
        '''
        print("Aqui é a primeira linha\n E aqui é a segunda linha")

    def linha_em_branco(self):
        '''
        Metodo para imprimir uma linha em branco para espaçamento.
        '''
        print("")

# Metodo principal (pono de partida)
if __name__ == "__main__":
    # Ceiando um objeto da classe mensagem
    mensagem = Mensagem() # Aqui 'mensagem' é uma instancia da classe Mensagem

    mensagem.mensagem_inicial()# Self aqui é o proprio objeto
    mensagem.mensagem_sem_quebra()# Chamando o metodo
    mensagem.mensagem_com_quebra()# Chamando o metodo
    mensagem.linha_em_branco()# Chamando o metodo
