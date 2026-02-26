notas_tuma = ['Joao',8,10,7, 'Maria',6,7,8, 'Jose',8,7,10, 'Claudia',10,7,9, 'ana',4,10,9]


nomes = []
notas_juntas = []

for i in range(len(notas_tuma)):
        if i % 4 == 0:
            notas_juntas.append(notas_tuma[i])
        else:
            nomes.append(notas_tuma[i])
            
print(f'{nomes}')
print(f'{notas_juntas}')