nota_1 = int(input('Digite a primeira nota: '))
nota_2 = int(input('digite a segunda nota: '))
nota_3 = int(input('Digite a terceira nota: '))

def media (nota_1,nota_2,nota_3):
    calculo = (nota_1 + nota_2 + nota_3) / 3
    print(f'a média das notas é {calculo}')
    
media(nota_1,nota_2,nota_3)