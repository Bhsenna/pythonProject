lista = input('Informe seus números: ').split()
i = 0
soma = 0

while i in range(len(lista)):
    try:
        lista[i] = int(lista[i])
        i += 1
    except:
        lista.pop(i)

lista.sort()
print(f'\33[32;1mCrescente: {lista}')  # da pra usar sorted(lista) também
lista.sort(reverse=True)
print(f'\33[31;1mDecrescente: {lista}')  # da pra usar sorted(lista, reverse=True) também
for i in range(len(lista)):
    soma += lista[i]
media = soma / len(lista)
print(f'\33[34;1mSoma: {soma}')
print(f'\33[33;1mMédia: {media:.2f}')