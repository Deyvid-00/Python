def dobrar(list):
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobrar(valores)
print(valores)