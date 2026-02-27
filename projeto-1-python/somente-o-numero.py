aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

preco_alguel = [valor for tipo, valor in aluguel if tipo == 'Apartamento']

print(f'{preco_alguel}')