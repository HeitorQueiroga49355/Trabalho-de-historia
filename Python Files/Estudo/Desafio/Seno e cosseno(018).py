from math import cos, sin, tan
from os import system
while True:
    print('=========================')
    print('Digite o ângulo: ')
    print('=========================')
    gra = int(input())
    au = gra / 57.2958
    coo = cos(au)
    sen = sin(au)
    taa = tan(au)
    print("O seno de {}° ângulo é: {:.2f}\nO cosseno de {}° ângulo é: {:.2f}\nA tangente de {}° ângulo é: {:.2f}".format(gra, sen, gra, coo, gra, taa))
    system('pause')
    system('cls')
