estudantes = ['joao','maria','jose','claudia','ana']

print(f'{estudantes}')

from random import randint

codigo_estudantes = []

def geracod():
    return str(randint(0,9999))

for i in range(len(estudantes)):
    codigo_estudantes.append((estudantes[i] , estudantes[i][0] + geracod()))
    
print(f'{codigo_estudantes}')


    