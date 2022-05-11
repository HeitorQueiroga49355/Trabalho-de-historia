alt = float(input('Qual é a sua altura? (m) '))
pes = float(input('Qual é o seu peso? (Kg) '))
imc = float(pes/alt**2)
print('O seu IMC é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso NORMAL!')
elif 18.5 <= imc < 25:
    print('Parabéns! Você está no peso IDEAL!')
elif 25 <= imc < 30:
    print('Você está ACIMA DO PESO!')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
else:
    print('Cuidado! Você  está em OBESIDADE MÓRBITA!!')
