def maior(*num):
    cont = maior = 0
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')


maior(2, 3, 1, 5, 7, 6)