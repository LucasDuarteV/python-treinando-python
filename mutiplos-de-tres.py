lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multi_de_t(lista_entrada):
    nova_lista = []
    for num in lista:
        if num % 3 == 0:
            nova_lista.append(num)
    return nova_lista

multi = multi_de_t(lista)

print(f'{multi}')