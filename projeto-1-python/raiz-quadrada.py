import math

numeros = [2, 8, 15, 23, 91, 112, 256]

for n in numeros:
    raiz = math.sqrt(n)
    
    if raiz // 1 == raiz:
        print(f'O número {n} possui raiz inteira {int(raiz)}')