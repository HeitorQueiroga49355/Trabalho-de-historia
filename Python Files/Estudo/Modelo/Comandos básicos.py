xxxxxx = input('\033[0;33;44mEsse é o documento que apresenta as funções básicas do python, e algumas dicas formatação de texto(maxi'
               'mize a tela).\nPressione "enter" para abrí-lo:')
print('\033[0;33;44m#'*190)
t = str('\033[0;33;44mTipos primitivos')
print('\033[0;33;44m {:=^100} '.format(t))
print('\033[0;33;44mAqui são os valores que os dígitos no python podem assumir:\n   ○ int = Para valores inteiros\n   ○ float = Par'
      '\033[0;33;44ma números reais\n   ○ bool = para valores lógicos(True ou false)\n   ○ str = Para caracteres')
t = str('\033[0;33;44mOperadores aritméticos')
print('\033[0;33;44m {:=^100} '.format(t))
print('\033[0;33;44mOs operadores aritméticos do python são:\n   ○ + = Para adição\n   ○ - = Para subtração\n   ○ * = Para multiplic'
      '\033[0;33;44mação\n   ○ ** = Para potenciação\n   ○ // = Para mostrar a parte inteira de uma divisão\n   ○ % = Para mostrar o'
      '\033[0;33;44m resto de uma divisão')
t = str("\033[0;33;44mOrdem de precedência")
print('\033[0;33;44m {:=^100} '.format(t))
print('\033[0;33;44mA ordem de precedência é:\n   1°: ()\n   2°: **\n   3°: *, / , // , %\n   4°: + , -')
t = str('\033[0;33;44mRadiciação')
print('\033[0;33;44m     {:*^90}'.format(t))
print('\033[0;33;44m      Para tirar a raiz de um número e não precisar importar nenhum módulo:\n       [*variável ou número]**(1/[o'
      '\033[0;33;44m número da raiz])')
print('\033[0;33;44m    ', '*'*90)
print('\033[0;33;44m ')
t = str('\033[0;33;44mFormatações do ".format"')
print('\033[0;33;44m {:=^100} '.format(t))
print('\033[0;33;44m   ○{:20}:   Para a frase aparecer em 20 caracteres\n   ○{:>20}:  Para a frase aparecer alinhada à direita\n   '
      '\033[0;33;44m○{:<20}:  Pra a frase aparecer alinhada á esquerda\n   ○{:^20}:  para a frase aparecer centralizada no espaço i'
      'ndicado\n   ○{:=^20}: Para a frase aparecer coberta pelo sinal e centralizada\n   ○{:.3f}:  Para os números apa'
      'recerem com 3 casas decimais\n   ○end='': Para continuar a próxima linha de programação na mesma, no resultado\n'
      '   ○[Barra contrária]n: Para quebrar a linha no resultado')
t = str('Manipulamento de textos em Python')
print(' {:=^100} '.format(t))
frase = 'Curso em vídeo'
print('frase = "Curso em vídeo Python"')
sb = ' Fatiamento '
print('|C |u |r |s |o |  |e |m |  |v |í |d |e |o |  |P |y |t |h |o |n |')
print('|0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|13|14|15|16|17|18|19|20|')
print('\n{:*^25}\nfrase[9]: Mostra apenas o caractere 9 da variável[v]\nfrase[9:13]: Mostra do caractere'
      ' 9 ao 12\nfrase[9:21]: Mostra do caractere 9 ao final\nfrase[9:21:2]: Mostra do caractere 9 ao final ao passo 2'
      '\nfrase[:5]: Mostra do primeiro caractere até o 4\nfrase[15:]: Mostra do caractere 5 até o final\nfrase[9::3]: M'
      'ostra do caractere 9 ao final ao passo 3'.format(sb))
sb = ' Análise '
print('\n{:*^25}\nlen(frase): Mostra o comprimento da frase\nfrase.count("o"): Mostra quantas vezes apar'
      'eceu a letra "o" na frase\nfrase.cont("o",0,13): Mostra a quantidade de "o" que apareceu do primeiro ao 12° cara'
      'ctere da frase\nfrase.find("deo"): Mostra a quantidade de vezes que apareceu a sentença na variável(se a sentenç'
      'a não existir o resultado será "-1")\n"Curso" in frase: dirá se existe a sentença entre parênteses na varíável, '
      'se sim, escreverá True'.format(sb))
sb = ' Transformação '
print('\n{:*^25}\n ○frase.repleace("Python", "Android"): Para substituir a primeira sentença entre parê'
      'nteses pela segunda\n ○frase.upper(): para transformar toda a varíavel em maiúscula\n ○frase.lower(): Para tran'
      'sformar toda a frase em minúsculas\n ○frase.capitalize(): Transforma toda a frase em minúsculas, porém a primeir'
      'a letra ficará maiúscula\n ○frase.title(): Todas as primeiras letras das palavras ficarão maiúsculas\n ○frase.s'
      'trip(): Para tirar todos os caracteres desnecessários no começo e no final da variável\n ○frase.rstrip(): Para t'
      'irar apenas os caracteres desnecessários da direita da variável\n ○frase.lstrip(): Para tirar os caracteres desn'
      'ecessários apenas da esquerda da variável'.format(sb))
sb = ' Divisão '
print("\n{:*^25}\n ○frase.split(): Divide as palavras da frase, nomeando por um índice para cada palavra(['a', 'b', 'c"
      "'])".format(sb))
sb = ' Junção '
print("")
print('\n', '#'*190, '\n')
print(frase.split())
xxxxxx = input('Pressione "enter" para fechar:')
