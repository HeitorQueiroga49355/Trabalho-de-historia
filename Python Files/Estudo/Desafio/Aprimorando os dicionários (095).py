tot = []
idc = int(0)
while True:
    dici = {}
    gols = []
    golstr = []
    totgols = 0
    listgols = []
    dici['nome'] = str(input('Nome do jogador: '))
    dici['qpartidas'] = int(input('Quantas partidas {} jogou?: '.format(dici['nome'])))
    for c in range(0, dici['qpartidas']):
        gols.append(int(input(f'   Quantos gols na partida {c + 1}: ')))
        totgols += gols[c]
        golstr.append(gols[c])
        gols.append(str(gols[c]))
        gols.pop(c)
    dici['qpartidas'] = str(dici['qpartidas'])
    golstr = str(golstr)
    dici['golstr'] = golstr
    dici['gols'] = gols
    listgols = str(gols)
    dici['listgols'] = listgols
    totgols = str(totgols)
    dici['totgols'] = totgols
    tot.append(dici)
    while True:
        cont = str(input('Quer continuar? [S / N] : ').lower().strip()[0])
        if cont in 'sn': break
        del cont
        print('ERRO! Digite apenas n ou s por favor.')
    idc += 1
    del dici
    del gols
    del golstr
    del totgols
    if cont == 'n': break
print('-=' * 70)
print('{:>3}{:>5}{:>16}{:>25}'.format('cod', 'nome', 'gols', 'total'))
print('-' * 50)
for c in range(0, idc):
   print('{:>3} {:<16}{:<25} {:>3}'.format(c, tot[c]['nome'], tot[c]['golstr'], tot[c]['totgols']))
while True:
    while True:
        idca = int(input('Mostrar levantamento de qual jogador? [Digite -1 para encerrar o programa]: '))
        if -1 <= idca < idc: break
        print('ERRO! Número inválido.')
    if idca == -1: break        
    print(' -- LEVANTAMENTO DO JOGADOR {}'.format(tot[idca]['nome']))
    ct = int(0)
    for c in tot[idca]['gols']:
        jogo = int(ct + 1)
        jogo = str(jogo)
        print('   No jogo {} fez {} gols.'.format(jogo, c))
        ct += 1
print('<< VOLTE SEMPRE >>')
