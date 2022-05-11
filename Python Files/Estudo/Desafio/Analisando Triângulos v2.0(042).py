a = float(input('Primeiro seguimento: '))
b = float(input('Segundo seguimento: '))
c = float(input('Terceiro seguimento: '))
if a + c > b and a + b > c and b + c > a:
    if a == b == c:
        print("Os seguimentos acima PODE FORMAR um triângulo EQUILÁTERO.")
    elif a == b != c or a == c != b or b == c != a:
        print('Os seguimentos acima PODE FORMAR um triângulo ISÓCELES.')
    else:
        print('Os seguimentos acima PODE FORMAR um triângulo ESCALENO ')
else:
    print('Os seguimentos acima não podem formar um triângulo.')
