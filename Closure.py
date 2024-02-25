

def criar_sudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar
    

s1 = criar_sudacao('Bom dia')
s2 = criar_sudacao('Boa noite')
print(s1('Deyvid'))
print(s2('Deyvid'))