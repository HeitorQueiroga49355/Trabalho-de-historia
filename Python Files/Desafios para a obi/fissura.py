n, f = map(int, input().split())
listastr = []
for i in range(n):
    lista = []
    numstr = str(input())
    for c in range(n):
        lista.append(numstr[c])
    listastr.append(lista)
cont = True
while cont == True:
    cont = bool(False)
    for i in range(len(listastr)):
        for c in range(len(listastr)):
            if listastr[i][c] != '*' and int(listastr[i][c]) <= f:
                if i == 0:
                    if c == 0:
                        listastr[i][c] = '*'
                        cont = True
                    elif c == n-1:
                        if listastr[i][c-1] == '*' or listastr[i+1][c-1] == '*' or listastr[i+1][c] == '*':
                            listastr[i][c] = '*'
                            cont = True
                    else:
                        if listastr[i][c-1] == '*' or listastr[i+1][c-1] == '*' or listastr[i+1][c] == '*' or listastr[i+1][c+1] == '*' or listastr[i][c+1] == '*':
                            listastr[i][c] = '*'
                            cont = True
                elif 0 < i < n - 1:
                    if c == 0:
                        if listastr[i-1][c] == '*' or listastr[i-1][c+1] == '*' or listastr[i][c+1] == '*' or listastr[i+1][c+1] == '*' or listastr[i+1][c] == '*':
                            listastr[i][c] = '*'
                            cont = True
                    elif c == n - 1:
                        if listastr[i-1][c] == '*' or listastr[i-1][c-1] == '*' or listastr[i][c-1] == '*' or listastr[i+1][c-1] == '*' or listastr[i+1][c] == '*':
                            listastr[i][c] = '*'
                            cont = True       
                    else:
                        if listastr[i+1][c] == '*' or listastr[i+1][c-1] == '*' or listastr[i][c-1] == '*' or listastr[i-1][c-1] == '*' or listastr[i-1][c] == '*' or listastr[i-1][c+1] == '*' or listastr[i][c+1] == '*' or listastr[i+1][c+1] == '*':
                            listastr[i][c] = '*'
                            cont = True     
                else:
                    if c == 0:
                        if listastr[i-1][c] == '*' or listastr[i-1][c+1] == '*' or listastr[i][c+1] == '*':
                            listastr[i][c] = '*'
                            cont = True
                    elif c == n - 1:
                        if listastr[i][c-1] == '*' or listastr[i-1][c-1] == '*' or listastr[i-1][c] == '*':
                            listastr[i][c] = '*'
                            cont = True       
                    else:
                        if listastr[i][c-1] == '*' or listastr[i-1][c-1] == '*' or listastr[i-1][c] == '*' or listastr[i-1][c+1] == '*' or listastr[i][c+1] == '*':
                            listastr[i][c] = '*'
                            cont = True
for i in range(n):
    for c in range(n):
        print(listastr[i][c], end = '')
    print()