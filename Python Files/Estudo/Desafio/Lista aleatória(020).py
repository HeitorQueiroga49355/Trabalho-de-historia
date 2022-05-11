from random import sample
a0 = str(input('Digite o nome do primeiro aluno:'))
a1 = str(input('Digite o nome do segundo aluno:'))
a2 = str(input('Digite o nome do terceiro aluno:'))
a3 = str(input('Digite o nome do quanto aluno:'))
se = sample([a0, a1, a2, a3], k=4)
print('A orde de apresentação será:\n', se)
