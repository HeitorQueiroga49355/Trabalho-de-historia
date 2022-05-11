from datetime import date
ano = date.today().year
sexo = str(input('Digite seu sexo(Masculino ou Feminino): ').upper().strip())
print('Você \033[31mNÃO\033[m precisa se alistar.'if sexo == 'FEMININO' else '', end='')
if sexo == 'MASCULINO':
    nas = int(input('Digite o ano que você nasceu: '))
    if ano-nas < 18:
        print("""Quem nasceu em {} tem {} anos em {}.
Ainda faltam {} ano(s) para se alistar
Seu alistamento será em {}.""".format(nas, ano - nas, ano, nas + 18 - ano, nas + 18))
    elif ano-nas > 18:
        print("""Quem nasceu em {} tem {} anos em {}.
Você já deveria ter se alistado há {} ano(s).
Seu alistamento foi em {}""".format(nas, ano-nas, ano, ano - (nas+18), nas + 18))
    elif sexo == 'MASCULINO' and nas > ano:
        print('Data de nascimento inválida')
    else:
        print("""Quem nasceu em {} tem {} anos
Você deve se alistar \033[31mIMEDIATAMENTE\033[m.""".format(nas, ano - nas))
if sexo != 'MASCULINO' and sexo != 'FEMININO':
    print('Sexo não identificado.')
x = input('')
