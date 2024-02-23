def area(larg, comp):
    a = larg * comp
    print(f'A area do terreno é {a}m quadrados!')


print('Controle de Terrenos')
l = float(input('Qual a largura do terreno (m): '))
c = float(input('Qual o comprimento do terreno (m): ' ))
area(l, c)