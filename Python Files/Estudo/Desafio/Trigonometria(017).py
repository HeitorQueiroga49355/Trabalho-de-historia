from math import hypot
um = str(input('Digite a unidade de medida utlizada:'))
c1 = float(input('Digite o comprimento do primeiro cateto:'))
c2 = float(input('Digite o comprimento do segundo cateto:'))
hi = hypot(c1, c2)
print('O valaor da hipotenusa desse triângulo  é: {} {}.'.format(hi,um))
