print('\x1b[38;5;3mCALCULADORA DE FINANCIAMENTO\n')

valP = input('Valor Presente: R$ ')
while type(valP) != float:
    try:
        valP = float(valP)
    except:
        print('Número inválido, tente novamente')
        valP = input('Valor Presente: R$ ')

tax = input('Taxa de Juros Mensal (Porcentagem): ')
while type(tax) != float:
    try:
        tax = float(tax)
    except:
        print('Número inválido, tente novamente')
        tax = input('Taxa de Juros Mensal (Porcentagem): ')
tax = tax / 100

num = input('N° de meses: ')
while type(num) != int:
    try:
        num = int(num)
    except:
        print('Número inválido, tente novamente')
        num = input('N° de meses: ')

amo = input('Tipo de Amortização\n[1] PRICE\n[2] SAC\nResposta: ')
while type(amo) != int:
    try:
        amo = int(amo)
    except:
        print('Número inválido, tente novamente')
        amo = input('Tipo de Amortização\n[1] PRICE\n[2] SAC\nResposta: ')

print('          Valor da                                       Saldo')
print(' N°       Parcela        Amortização     Juros           devedor')
salD, valPaT, JurosT = valP, 0, 0
for i in range(num):
    if amo == 1:
        valPa = valP * ((((1+tax)**num)*tax) / (((1+tax)**num)-1))
        juros = salD * tax
        am = valPa - juros
        salD -= am
        JurosT += juros
        print(f'{i+1}'.center(3), 4 * ' ', f'R$ {valPa:.2f}'.center(8), 4 * ' ', f'R$ {am:.2f}'.center(8), 4 * ' ', f'R$ {juros:.2f}'.center(8), 4 * ' ', f'R$ {salD:.2f}')
    elif amo == 2:
        am = valP / num
        juros = salD * tax
        salD -= am
        valPa = am + juros
        valPaT += valPa
        JurosT += juros
        print(f'{i + 1}'.center(3), 4 * ' ', f'R$ {valPa:.2f}'.center(8), 4 * ' ', f'R$ {am:.2f}'.center(8), 4 * ' ', f'R$ {juros:.2f}'.center(8), 4 * ' ', f'R$ {salD:.2f}')

if amo == 1:
    print(f'Total    R$ {(valPa * num):.2f}     R$ {valP:.2f}     R$ {JurosT:.2f}')
elif amo == 2:
    print(f'Total    R$ {valPaT:.2f}     R$ {valP:.2f}     R$ {JurosT:.2f}')