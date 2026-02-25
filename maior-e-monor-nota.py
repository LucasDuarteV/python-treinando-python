lista = [10,8,5,7]

def desmpenho_aluno(notas):
    menor = min(lista)
    maior = max(lista)
    media = sum(lista) / len(lista)
    situacao = 'aprovado ' if media >= 7 else 'Reprovado(a)'
        
    
    return maior, menor, media, situacao

maior, menor, media, situcao = desmpenho_aluno(lista)

print(f'As notas do aluno(a) foi {lista}')
print(f'A média do aluno(a) foi {media}')
print(f'A menor nota do aluno(a) foi {menor}')
print(f'A maior nota do aluno(a) foi {maior}')
print(f'O aluno(a) foi {situcao}')