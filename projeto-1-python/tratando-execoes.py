notas = {'luan' : [9,10,7]}

try: 
    nome = input('Digite o nome do estudante: ')
    resultado = notas[nome]
except KeyError: 
    print(f'Estudante não matriculado(a)')
else:
    print(f'A nota do {nome} é {resultado}')