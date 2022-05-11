pn = float(input('Primeira nota:'))
sn = float(input('Segunda nota:'))
md = float((pn+sn)/2)
print('Tirando {} e {} a média do aluno é de {:.1f}'.format(pn, sn, md))
if md >= 6.0:
    print('O aluno está \033[32mAPROVADO\033[m.')
elif md < 6.0 and md > 5.0 or md == 5.0:
    print('O aluno está em \033[31mRECUPERAÇÃO\033[m.')
else:
    print('O aluno está \033[31mREPROVADO\033[m.')
