# Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo o resultado.
num = input('Informe o número: ')

if num.lstrip('-').isdigit():
    num = int(num)
    if num > 0:
        print(num * 2)
    elif num < 0:
        print(num * 3)
    else:
        print(0)
else:
    print('Não é um número')