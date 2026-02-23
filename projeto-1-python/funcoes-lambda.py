nota_1 = int(input('Diigite a nota do estudante: '))
nota_2 = int(input('Diigite a nota do estudante: '))
nota_3 = int(input('Diigite a nota do estudante: '))


media_ponderavel = lambda x , y , z: (x * 3 + y * 2 + z * 5) / 10
media_estudante = media_ponderavel(nota_1,nota_2,nota_3)
print(media_estudante)