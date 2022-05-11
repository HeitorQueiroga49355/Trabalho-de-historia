n, f = map(int, input().split())
listastr = []
for i in range(n):
    lista = []
    numstr = str(input())
    for c in range(n):
        lista.append(numstr[c])
    listastr.append(lista)
print(listastr[0][1])