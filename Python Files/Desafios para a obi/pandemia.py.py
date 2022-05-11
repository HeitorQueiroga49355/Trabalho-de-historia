tota, totr = map(int, input().split())
ami, pri = map(int, input().split())
listatot = []
for i in range(totr):
    listaam = [int(c) for c in input().split()]
    listaam.pop(0)
    listatot.append(listaam)
lista_infectados = [ami]
for i in range(pri - 1, totr):
    pres = False
    for x in listatot[i]:
        if x in lista_infectados:
          pres = True
    for c in range(len(listatot[i])):
        if listatot[i][c] not in lista_infectados and pres == True:
            lista_infectados.append(listatot[i][c])
print(len(lista_infectados))
