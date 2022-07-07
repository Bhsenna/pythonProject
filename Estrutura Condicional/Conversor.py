print(42*'-')
print('Selecione uma opção'.center(42))
print(42*'-')
print('''1 - Converter de Celsius para Kelvin
2 - Converter de Celsius para Fahrenheit
3 - Converter de Kelvin para Celsius
4 - Converter de Kelvin para Fahrenheit
5 - Converter de Fahrenheit para Celsius
6 - Converter de Fahrenheit para Kelvin''')

op = int(input('Opção (1-6): '))

if op == 1 or op == 2:
    temp1 = float(input('Digite a temperatura em Celsius: '))
    if temp1 < -273.15:
        print('MUITO FRIO! NÃO DESCE MAIS DO QUE ISSO! Tente outro valor.')
    elif op == 1:
        temp2 = temp1 + 273.15
        print(f'Temperatura em Kelvin: {temp2:.2f}°K')
    elif op == 2:
        temp2 = (temp1 * 1.8) + 32
        print(f'Temperatura em Fahrenheit: {temp2:.2f}°F')
elif op == 3 or op == 4:
    temp1 = float(input('Digite a temperatura em Kelvin: '))
    if temp1 < 0:
        print('MUITO FRIO! NÃO DESCE MAIS DO QUE ISSO! Tente outro valor.')
    elif op == 3:
        temp2 = temp1 - 273.15
        print(f'Temperatura em Celsius: {temp2:.2f}°C')
    elif op == 4:
        temp1 = temp1 - 273.15
        temp2 = (temp1 * 1.8) + 32
        print(f'Temperatura em Fahrenheit: {temp2:.2f}°F')
elif op == 5 or op == 6:
    temp1 = float(input('Digite a temperatura em Fahrenheit : '))
    if temp1 < -459.67:
        print('MUITO FRIO! NÃO DESCE MAIS DO QUE ISSO! Tente outro valor.')
    elif op == 5:
        temp2 = (temp1 - 32) / 1.8
        print(f'Temperatura em Celsius: {temp2:.2f}°C')
    elif op == 6:
        temp2 = ((temp1 - 32) / 1.8) + 273.15
        print(f'Temperatura em Kelvin: {temp2:.2f}°K')
else:
    print('Selecione uma opção válida')