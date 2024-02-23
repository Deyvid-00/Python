import os
lista = []

while True:
    print('Selecione uma opção')
    option = input('[i]nserir, [a]pagar, [l]istar:')

    if option == 'i':
        os.system('CLS')
        valor = input('Valor:')
        lista.append(valor)
    elif option == 'a':
        os.system('CLS')
        indice = int(input('Digite um indíce para apagar:'))
        del lista[indice]
    elif option == 'l':
        os.system('CLS')
        if len(lista) == 0:
            print('Não tem anda para listar')
        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')