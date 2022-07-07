lista = input('Informe valores aleatórios (separados por Espaço): ').split()
I, S, F, B = 0, 0, 0, 0
for i in range(len(lista)):
    try:
        lista[i] = int(lista[i])
        I += 1
    except:
        try:
            lista[i] = float(lista[i].replace(',', '.'))
            F += 1
        except:
            if lista[i].lower() == 'true':
                lista[i] = True
                B += 1
            elif lista[i].lower() == 'false':
                lista[i] = False
                B += 1
            else:
                S += 1
                continue

lista.reverse()
print(lista)
print(f'''Int: {I}
String: {S}
Float: {F}
Bool: {B}''')