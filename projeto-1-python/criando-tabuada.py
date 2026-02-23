def gerear_tabuada():
    
    num = int(input('Digite o número da tabuada que será gerada: '))
    
    print(f'A tabuada que será gerada é {num}')
    
    for i in range(0,11):
        resultado = i * num
        print(f'{num} X {i} = {resultado}')
    
gerear_tabuada()