'''
Classe responsável por exibir o menu e capturar a
opção escolhida
'''
class Menu:
    @staticmethod
    def exibir_menu():
        '''
        Método estático para exibir as opções de pagamento
        '''
        print("\n-- Menu de Forma de Pagamento --\n")
        print("1 - Venda a vista - desconto de 10%")
        print("2 - Venda a prazo 30 dias - desconto de 5%")
        print("3 - Venda a prazo 60 dias - preço normal")
        print("4 - Venda a prazo 90 dias - acréscimo de 5%")
        print("5 - Venda com cartão de dpebito - desconto de 8%")
        print("6 - Venda com cartão de crédito - acréscimo de 7%")

    @staticmethod
    def obter_opcao():
        '''
        Método estático para solicitar e validar a opção
        do usuário
        '''
        while True:
            try:
                opcao=int(input("Escolha uma opção (1 a 6): "))
                if 1<=opcao<=6:
                    return opcao
                else:
                    print("Opção inválida! Digite um número entre 1 e 6")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro (1 a 6)")