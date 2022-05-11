from datetime import date
nas = int(input('Digite o ano que você nasceu: '))
idd = int(date.today().year-nas)
print('O atleta tem {} anos.'.format(idd))
if idd <= 9:
    print('Classificação: MIRIM')
elif 9 < idd <= 14:
    print('Classificação: INFANTIL')
elif 14 < idd <= 19:
    print('Classificação: JÚNIOR')
elif 19 < idd <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
