notas = [10,8,10,10]
aluno = 'Luan Duarte'
def boletim(notas):
    media = sum(notas) / len(notas)
    
    if media >= 6:
        situacao = 'Aprovado(a)'
    else:
        situacao = 'Reprovado(a)'
    
    return(media,situacao)

media_final , situacao_final = boletim(notas)

print(f'O aluno {aluno} fechou o ano letivo com a média de {media_final} e com a situação de {situacao_final}')