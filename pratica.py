def dduplicar(num):
    return num * 2, num * 3, num * 4

# Jeito mais pratico

def criar_multiplicador(multplicador):
    def multiplicar(numero):
        return numero * multplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))


n = dduplicar(2)
print(n)