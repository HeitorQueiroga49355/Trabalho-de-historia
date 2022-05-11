#Desafio 35
l1 = float(input('Digie a medida do primerio lado(use em uma mesma unidade de medida para todos os lados):'))
l2 = float(input('Digite a medida do segundo lado do triângulo:'))
l3 = float(input('Digite a medida do terceiro lado do triângulo:'))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
  print('Esse triângulo tem medida possíveis de ser montados.')
else:
  print('As medidas não é possível formar um triângulo.\033[0;33;44m')
