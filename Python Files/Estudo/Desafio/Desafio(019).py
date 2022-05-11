from random import choice
n0 = str(input('Digite o primeiro nome:'))
n1 = str(input('Digite o segundo nome:'))
n2 = str(input('Digite o terceiro nome:'))
n3 = str(input('Digite o quarto nome:'))
print('O aluno selecionado foi:{}'.format(choice([n0, n1, n2, n3])))
