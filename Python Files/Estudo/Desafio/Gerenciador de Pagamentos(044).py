print('{:=^40}'.format('Loja Heitor'))
pre = float(input('Digite o preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais vezes no cartão''')
op = int(input('Qual é a opção: '))
if op == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(pre, pre-(pre/100*10)))
elif op == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(pre, pre-(pre/100*5)))
elif op == 3:
    print('Sua compra de {} será parcelada e 2x de {:.2f}, custando {:.2f} no final.'.format(pre, pre/2, pre))
elif op == 4:
    par = int(input('Em quantas parcelas deseja pagar: '))
    print('''Sua compra será parcelada em {} vezes de R${} COM JUROS.
Sua compra de R${} ficará por R${} no final.'''.format(par, ((pre/100*20)+pre)/par, pre, pre+(pre/100*20)))
else:
    print('Digite um opção válida.')
