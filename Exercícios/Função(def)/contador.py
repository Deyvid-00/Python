def contador(i, f, p):

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print(f'contagem de {i} ate o {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' - ')
            cont += p
        print('fim!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' - ')
            cont -= p
        print('fim!')

contador(1, 12, 1)
contador(10, 0, 1)

print('Sua vez de personalizar o contador!')
inicio = int(input('ínicio: '))
fim = int(input('fim: '))
passos = int(input('passos: '))
contador(inicio, fim, passos)