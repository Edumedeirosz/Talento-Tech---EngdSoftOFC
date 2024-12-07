#Banco fictício
nome = str(input('Diga seu nome: \n')).lower()
sen = 13579
#Incremento feito para testes, com objetivo de criar um banco de dados futuramente para a utilização do "banco para vários usuários."
val = int(input('Diga sua senha: '))
enc = 0
sal = 0.00
if val == sen and nome == 'eduardo medeiros da paz':
    while enc != -1:
        sel = int(input('Bem-vindo ao banco, {}. Seu saldo atual é de R${}! O que você deseja fazer?\n1.DEPÓSITO\n2.SAQUE\n3.TRANSFERÊNCIA\n4.SAIR\n'.format(nome, sal)))
        #Transferência, outro "pedaço" que poderia ser atualizado ou incrementado futuramente.
        if sel == 1:
            dep = float(input('Diga o valor a ser depositado: \n'))
            sal = sal + dep
            print('Seu saldo atual é de R${}.\n'.format(sal))
        elif sel == 2:
            if sal >= 0:
                saq = int(input('Diga o valor de saque:\n'))
                sal = sal - saq
                print('Seu saldo atual é de R${}.\n'.format(sal))
            else:
                print('Valor inválido.')
        elif sel == 3:
            print('\nImplementação em breve.\n')
            #Como dito antes, há um aviso breve sobre sua futura implementação.
        elif sel == 4:
            fim = -1
            print('Obrigado por usar o banco!')
            enc = fim
            #Outra coisa que deveria futuramente ser implementada é uma forma de salvar os dados da conta bancária do usuário na nuvem.
else:
    print('Usuário não encontrado ou senha inválida.')
