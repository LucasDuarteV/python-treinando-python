import random

nome = input('Digite o seu nome: ')

token = random.randrange(1000,9998,2)

print(f'{nome} o seu token de acesso é {token}')