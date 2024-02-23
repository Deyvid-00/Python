# cpf_usuario = '746.824.890-70'.replace('.','').replace('-','').replace(' ','') #CPF qualquer.

entrada = input('CPF: ').replace('.','').replace('-','').replace(' ','')

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('Dados sequenciais inválidos')

nove_digitos = entrada[:9] #Separando os 9 primeiros digitos, usando modo de cortar strings.
contador_1 = 10
soma_1 = 0
for digito_1 in nove_digitos: #Loop for para pecorrer os 9 primeiros digitos do CPF e o contador regressivamente ate 2. E então multiplicando-os.
    soma_1 += (int(digito_1)*contador_1)
    contador_1 -= 1

digito_1 = (soma_1 * 10) % 11 #Terminando com ultimos 2 calculos de verificar o primeiro digito do CPF.

# digito_1 = digito_1 if digito_1 <= 9 else 0

if digito_1 > 9: #Se o Digito_1 for maior que 9 o digito do CPF recebe 0 caso não for tera o valor já recebido.
    digito_1 = 0
else:
    digito_1 = digito_1

dez_digitos_2 = entrada[:9] + str(digito_1)

contador_2 = 11
soma_2 = 0
for digito_2 in dez_digitos_2:
    soma_2 += (int(digito_2) * contador_2)
    contador_2 -= 1

digito_2 = (soma_2 * 10) % 11

digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_calculado == entrada:
    print(f'{cpf_calculado} é válido')
else:
    print(f'{entrada} é inválido')