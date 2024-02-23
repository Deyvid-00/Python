import random

nove_digitos = ''
contador_1 = 10
soma = 0

for i in range(9):
    nove_digitos += str(random.randint(0, 9))

for digito in nove_digitos:
    soma += int(digito)*contador_1
    contador_1 -= 1

d_1 = (soma * 10) % 11
d_1 = d_1 if d_1 <= 9 else 0

dez_digitos = nove_digitos + str(d_1)
contador_2 = 11
soma_2 = 0

for digito in dez_digitos:
    soma_2 += int(digito)*contador_2
    contador_2 -= 1

d_2 = (soma_2 * 10) % 11
d_2 = d_2 if d_2 <= 9 else 0

cpf_calculado = f'{nove_digitos}{d_1}{d_2}'

print(cpf_calculado)