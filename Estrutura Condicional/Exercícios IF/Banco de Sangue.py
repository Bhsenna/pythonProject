# Banco de Sangue. O Banco de sangue do HEMOSC está com estoque baixo de
# para alguns tipos. Faça um programa que pergunte a idade da pessoa, e seu tipo sanguíneo.
# Caso a pessoa queira doar sangue  ou retirar sangue(Fazer a pergunta). Caso sim,
# o estoque do tipo de sangue que a pessoa informou será atualizado com o novo saldo.
# Ao final, informar o saldo do estoque para cada tipo sanguíneo;

# Restrições:
# O estoque máximo do banco não pode passar de 200 bolsas
# A doação só pode ser 1 bolsa por pessoa
# A retirada deve ser feita em múltiplos de 5 bolsas (5, 10, 15, 20)
# Pessoas acima de 65 anos não podem doar

import random

A1, A2, B1, B2, AB1, AB2, O1, O2 = random.randint(0, 200), random.randint(0, 200), random.randint(0,
                                                                                                  200), random.randint(
    0, 200), random.randint(0, 200), random.randint(0, 200), random.randint(0, 200), random.randint(0, 200)

idade = int(input('Informe a sua idade: '))
tipo = int(input('Selecione o seu tipo sanguíneo:\n(1) A\n(2) B\n(3) AB\n(4) O\n'))
Rh = int(input('Selecione o seu Fator RH:\n(1) Positivo\n(2) Negativo\n'))
op = int(input('Você quer:\n(1) Doar Sangue\n(2) Retirar Sangue\n'))
print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas\n\n''')

if tipo == 1:
    if Rh == 1:
        if op == 1:
            if idade > 65 or idade < 18:
                print('Você não pode doar sangue com essa idade!')
            else:
                if A1 < 200:
                    print('Doação completa')
                    A1 += 1
                    print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
                else:
                    print('Esse banco já está com o estoque cheio, não há como doar!')
        elif op == 2:
            ret = int(input('Informe a quantidade de bolsas que você deseja retirar: '))
            if ret % 5 != 0:
                print('Só pode retirar em multiplos de 5')
            elif ret >= A1:
                print('Não há bolsas o suficiente para serem retiradas')
            else:
                print('Bolsas retiradas com sucesso')
                A1 -= ret
                print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
        else:
            print('Opção inválida')
    elif Rh == 2:
        if op == 1:
            if idade > 65 or idade < 18:
                print('Você não pode doar sangue com essa idade!')
            else:
                if A2 < 200:
                    print('Doação completa')
                    A2 += 1
                    print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
                else:
                    print('Esse banco já está com o estoque cheio, não há como doar!')
        elif op == 2:
            ret = int(input('Informe a quantidade de bolsas que você deseja retirar: '))
            if ret % 5 != 0:
                print('Só pode retirar em multiplos de 5')
            elif ret >= A2:
                print('Não há bolsas o suficiente para serem retiradas')
            else:
                print('Bolsas retiradas com sucesso')
                A2 -= ret
                print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
        else:
            print('Opção inválida')
    else:
        print('Tipo Sanguíneo inválido')
elif tipo == 2:
    if Rh == 1:
        if op == 1:
            if idade > 65 or idade < 18:
                print('Você não pode doar sangue com essa idade!')
            else:
                if B1 < 200:
                    print('Doação completa')
                    B1 += 1
                    print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
                else:
                    print('Esse banco já está com o estoque cheio, não há como doar!')
        elif op == 2:
            ret = int(input('Informe a quantidade de bolsas que você deseja retirar: '))
            if ret % 5 != 0:
                print('Só pode retirar em multiplos de 5')
            elif ret >= B1:
                print('Não há bolsas o suficiente para serem retiradas')
            else:
                print('Bolsas retiradas com sucesso')
                B1 -= ret
                print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
        else:
            print('Opção inválida')
    elif Rh == 2:
        if op == 1:
            if idade > 65 or idade < 18:
                print('Você não pode doar sangue com essa idade!')
            else:
                if B2 < 200:
                    print('Doação completa')
                    B2 += 1
                    print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
                else:
                    print('Esse banco já está com o estoque cheio, não há como doar!')
        elif op == 2:
            ret = int(input('Informe a quantidade de bolsas que você deseja retirar: '))
            if ret % 5 != 0:
                print('Só pode retirar em multiplos de 5')
            elif ret >= B2:
                print('Não há bolsas o suficiente para serem retiradas')
            else:
                print('Bolsas retiradas com sucesso')
                B2 -= ret
                print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
        else:
            print('Opção inválida')
    else:
        print('Tipo Sanguíneo inválido')
elif tipo == 3:
    if Rh == 1:
        if op == 1:
            if idade > 65 or idade < 18:
                print('Você não pode doar sangue com essa idade!')
            else:
                if AB1 < 200:
                    print('Doação completa')
                    AB1 += 1
                    print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
                else:
                    print('Esse banco já está com o estoque cheio, não há como doar!')
        elif op == 2:
            ret = int(input('Informe a quantidade de bolsas que você deseja retirar: '))
            if ret % 5 != 0:
                print('Só pode retirar em multiplos de 5')
            elif ret >= AB1:
                print('Não há bolsas o suficiente para serem retiradas')
            else:
                print('Bolsas retiradas com sucesso')
                AB1 -= ret
                print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
        else:
            print('Opção inválida')
    elif Rh == 2:
        if op == 1:
            if idade > 65 or idade < 18:
                print('Você não pode doar sangue com essa idade!')
            else:
                if AB2 < 200:
                    print('Doação completa')
                    AB2 += 1
                    print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
                else:
                    print('Esse banco já está com o estoque cheio, não há como doar!')
        elif op == 2:
            ret = int(input('Informe a quantidade de bolsas que você deseja retirar: '))
            if ret % 5 != 0:
                print('Só pode retirar em multiplos de 5')
            elif ret >= AB2:
                print('Não há bolsas o suficiente para serem retiradas')
            else:
                print('Bolsas retiradas com sucesso')
                AB2 -= ret
                print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
        else:
            print('Opção inválida')
    else:
        print('Tipo Sanguíneo inválido')
elif tipo == 4:
    if Rh == 1:
        if op == 1:
            if idade > 65 or idade < 18:
                print('Você não pode doar sangue com essa idade!')
            else:
                if O1 < 200:
                    print('Doação completa')
                    O1 += 1
                    print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
                else:
                    print('Esse banco já está com o estoque cheio, não há como doar!')
        elif op == 2:
            ret = int(input('Informe a quantidade de bolsas que você deseja retirar: '))
            if ret % 5 != 0:
                print('Só pode retirar em multiplos de 5')
            elif ret >= O1:
                print('Não há bolsas o suficiente para serem retiradas')
            else:
                print('Bolsas retiradas com sucesso')
                O1 -= ret
                print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
        else:
            print('Opção inválida')
    elif Rh == 2:
        if op == 1:
            if idade > 65 or idade < 18:
                print('Você não pode doar sangue com essa idade!')
            else:
                if O2 < 200:
                    print('Doação completa')
                    O2 += 1
                    print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
                else:
                    print('Esse banco já está com o estoque cheio, não há como doar!')
        elif op == 2:
            ret = int(input('Informe a quantidade de bolsas que você deseja retirar: '))
            if ret % 5 != 0:
                print('Só pode retirar em multiplos de 5')
            elif ret >= O2:
                print('Não há bolsas o suficiente para serem retiradas')
            else:
                print('Bolsas retiradas com sucesso')
                O2 -= ret
                print(f'''Bancos:
A+: {A1} bolsas
A-: {A2} bolsas
B+: {B1} bolsas
B-: {B2} bolsas
AB+: {AB1} bolsas
AB-: {AB2} bolsas
O+: {O1} bolsas
O+: {O2} bolsas''')
        else:
            print('Opção inválida')
    else:
        print('Tipo Sanguíneo inválido')
else:
    print('Tipo Sanguíneo inválido')
