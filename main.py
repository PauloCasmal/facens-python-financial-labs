from models.transaction import Transaction

class Initialize():


    #def __init__(self):



    def show_menu(self):
        print(50 * '-')
        print('Bem-vindo ao Controle Financeiro')
        print(50 * '-')

        print('1 - Adicionar transação')
        print('2 - Visualizar transações')
        print('3 - Sair')

    
    def choose_option(self):
        option = input('\nEscolha uma das opções: ')
        
        if option not in ['1', '2', '3']:
            print('\nOpção inválida!')

        return option

    
    def add(self):
        operation = input('\nInforme o tipo da operação: ')
        value = input('\nInforme o valor da operação: ')
        description = input('\nInforme a descrição: ')

        transaction = Transaction(operation, value, description)
        transaction.save()

        del transaction


    def view(self):
        Transaction().view() #static class

    def exit(self):
        print('\nObrigado, volte sempre!')


if __name__ == '__main__':
    init = Initialize()
    option = ''

    while option != '3':
        init.show_menu()
        option = init.choose_option()

        if option == '1':
            init.add()
        elif option == '2':
            init.view()
        elif option == '3':
            init.exit()

