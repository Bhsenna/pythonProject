anos = input('Insira os anos: ').split()

cont = 0
while cont < len(anos):
    if anos[cont].lstrip('0').isnumeric():
        anos[cont] = int(anos[cont])
        cont += 1
    else:
        anos.pop(cont)

par, impar, bi, pas, fut = 0, 0, 0, 0, 0
cont = 0
while cont < len(anos):
    if not anos[cont] % 2:
        par += 1
    else:
        impar += 1

    if not anos[cont] % 4:
        if not anos[cont] % 100 and anos[cont] % 400:
            if not (anos[cont] / 100) % 4:
                bi += 1
        else:
            bi += 1

    if anos[cont] > 2022:
        fut += 1

    if anos[cont] < 2022:
        pas += 1
    cont += 1

print(f'''Dos {len(anos)} selecionados:
{par} eram pares
{impar} eram impares
{bi} eram bissextos
{fut} são futuros
{pas} são passados''')