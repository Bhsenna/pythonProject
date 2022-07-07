import random, webbrowser
rep = "S"
while rep == "S":
    print("\x1b[38;5;124m\x1b[1mDigite 1 para validar um código de barras EAN-8 (8 dígitos)\n")
    print("\x1b[38;5;13mDigite 2 para validar um código de barras EAN-13 (13 dígitos)\n")
    print("\x1b[38;5;214mDigite 3 para gerar um código de barras EAN-8 (8 dígitos)\n")
    print("\x1b[38;5;24mDigite 4 para gerar um código de barras EAN-13 (13 dígitos)\n")
    print("\x1b[38;5;55mDigite 5 para procurar seu código de barras na Amazon.com\n")
    digito = input("\x1b[0m\x1b[3m\x1b[38;5;111mDigite aqui: \x1b[0m\n")

    while digito != "1" and digito != "2" and digito != "3" and digito != "4" and digito != "5":
        print("Dígito errado. Digite novamente, por favor: \n")
        digito = input("Digite aqui: \n")
        if digito == ("1" or "2" or "3" or "4" or "5"):
            break

    cont2, cont, calc, calc2, cont3 = 0, 0, 0, 0, 1
    if digito == "1":
        cod = input("\x1b[0m\x1b[38;5;124mInsira seu código de 8 dígitos:\x1b[0m\n")
        cod8 = cod[7]
        cod = cod[:7]
        while cont < 4:
            calc += int(cod[cont2]) * 3
            cont2 += 2
            if cont < 3:
                calc2 += int(cod[cont3])
                cont3 += 2
            cont += 1
        res = (calc + calc2) % 10
        if res != 0:
            res1 = 10 - res
        else:
            res1 = 0

        if cod8 == str(res1):
            print("\n\x1b[1m\x1b[38;5;76m Código de barras válido. \x1b[0m\n")
        else:
            print("\n\x1b[1m\x1b[38;5;160m Código de barras inválido. \x1b[0m\n")

    if digito == "2":
        cod = input("\x1b[38;5;13mInsira seu código de 13 dígitos: \n")
        cod13 = cod[12]
        cod = cod[:12]
        while cont < 6:
            calc += int(cod[cont3]) * 3
            cont3 += 2
            calc2 += int(cod[cont2])
            cont2 += 2
            cont += 1
        res = (calc + calc2) % 10
        if res != 0:
            res2 = 10 - res
        else:
            res2 = 0

        if cod13 == str(res2):
            print("\n\x1b[1m\x1b[38;5;76m Código de barras válido. \x1b[0m\n")
        else:
            print("\n\x1b[1m\x1b[38;5;160m Código de barras inválido. \x1b[0m\n")

    if digito == "1" or digito == "2":
        if cod[0:3] == "789" or cod[0:3] == "790":
            print("\x1b[38;5;76m O país de cadastramento desse produto é o Brasil. \n")
        elif cod[0:3] == "759":
            print("\x1b[38;5;76m O país de cadastramento desse produto é a Venezuela. \n")
        elif cod[0:3] == "770" or cod[0:3] == "771":
            print("\x1b[38;5;76m O país de cadastramento desse produto é a Colômbia. \n")
        elif cod[0:3] == "773":
            print("\x1b[38;5;76m O país de cadastramento desse produto é o Uruguai. \n")
        elif cod[0:3] == "775":
            print("\x1b[38;5;76m O país de cadastramento desse produto é o Peru. \n")
        elif cod[0:3] == "777":
            print("\x1b[38;5;76m O país de cadastramento desse produto é a Bolívia. \n")
        elif cod[0:3] == "778" or cod[0:3] == "779":
            print("\x1b[38;5;76m O país de cadastramento desse produto é a Argentina. \n")
        elif cod[0:3] == "780":
            print("\x1b[38;5;76m O país de cadastramento desse produto é o Chile. \n")
        elif cod[0:3] == "784":
            print("\x1b[38;5;76m O país de cadastramento desse produto é o Paraguai. \n")
        elif cod[0:3] == "786":
            print("\x1b[38;5;76m O país de cadastramento desse produto é o Equador. \n")
        else:
            print("\x1b[38;5;160m O país cadastrado não faz parte da nossa lista. \n")

    if digito == "3":
        pa = int(input("""\x1b[38;5;214m\x1b[3mSelecione o país de cadastramento do produto:\x1b[0m\x1b[38;5;214m
0- Equador
1 - Brasil
2 - Venezuela
3 - Colômbia
4- Uruguai
5- Peru
6- Bolivia
7- Argentina
8- Chile
9- Paraguai
10- País aleatório\n"""))
        pal = ['786', '789', '759', '770', '773', '775', '777', '778', '780', '784', f'{str(random.randint(0, 9))}{str(random.randint(0, 9))}{str(random.randint(0, 9))}']
        if random.randint(0, 1) == 1:
            pal[1], pal[3], pal[7] = '790', '771', '779'
        cont = 3
        cod = pal[pa]
        while cont < 7:
            c = random.randint(0, 9)
            cod = f'{cod}{c}'
            cont += 1
        cont = 0
        while cont < 4:
            calc += int(cod[cont2]) * 3
            cont2 += 2
            if cont < 3:
                calc2 += int(cod[cont3])
                cont3 += 2
            cont += 1
        res = (calc + calc2) % 10
        if res != 0:
            res1 = 10 - res
            print(f'\x1b[38;5;124m{cod + str(res1)}')
        else:
            print(f'\x1b[38;5;124m{cod + str(res)}')

    if digito == "4":
        pa = int(input("""\x1b[38;5;24m\x1b[3mSelecione o país de cadastramento do produto:\x1b[0m\x1b[38;5;24m
0- Equador
1 - Brasil
2 - Venezuela
3 - Colômbia
4- Uruguai
5- Peru
6- Bolivia
7- Argentina
8- Chile
9- Paraguai
10- País aleatório\n"""))
        pal = ['786', '789', '759', '770', '773', '775', '777', '778', '780', '784', f'{str(random.randint(0, 9))}{str(random.randint(0, 9))}{str(random.randint(0, 9))}']
        if random.randint(0, 1) == 1:
            pal[1], pal[3], pal[7] = '790', '771', '779'
        cont = 3
        cod = pal[pa]
        while cont < 12:
            c = random.randint(0, 9)
            cod = f'{cod}{c}'
            cont += 1
        cont = 0
        while cont < 6:
            calc += int(cod[cont3]) * 3
            cont3 += 2
            calc2 += int(cod[cont2])
            cont2 += 2
            cont += 1
        res = (calc + calc2) % 10
        if res != 0:
            res2 = 10 - res
            print(f'\x1b[38;5;13m{cod + str(res2)}')
        else:
            print(f'\x1b[38;5;13m{cod + str(res)}')

    if digito == "5":
        cod = input("\n\x1b[38;5;55m Insira seu código de barras: \n")
        webbrowser.open(f"https://www.amazon.com.br/s?k={cod}")

    print("\x1b[0m\x1b[3m\x1b[38;5;111mHá mais algum código de barras para validar? \n")
    rep = input("Responda com S ou N: \n").upper()