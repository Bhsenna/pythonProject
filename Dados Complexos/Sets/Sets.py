
lista1 = list(range(5, 11))
lista2 = [3, 5, 7, 9, 3]
# Transformar em ser(conjunto)
set1 = set(lista1)
set2 = set(lista2)  # Set não tem valores duplicados, o segundo 3 desaparece


# if len(lista2) == len(set2):
#     print('sem duplicadas')
# else:
#     print('duplicadas')

# imprimir um set
print(f'Set 2 {set2}')
print(f'Set 1 {set1}')

set3 = {4, 5, 6, 7, 9}
print(type(set3))

# Não é possível alterar um item já criado do set
# Apenas deletar e inserir outro


# juntar 2 sets
print(f'Union {set2.union(set1)}')


# verificar a interseção entre 2 sets
print(f'Interseção {set2.intersection(set1)}')


# verificar diferença entre 2 sets
print(f'Difference {set2.difference(set1)}')
print(f'Difference {set1.difference(set2)}')

# verificar diferença simétrica entre 2 sets
print(f'Symmetric Difference {set2.symmetric_difference(set1)}')


# verificar se um item esá no set:
if 9 in set2:
    print('encontrei')


# adicionar items ao set
set2.add(25)
set1.add(14)
print(set1)
print(set2)


# Adicionar uma lista nova ao set
tupla1 = (3, 5, 13, 290)
lista3 = [260, 220, 240]
set2.update(tupla1)
print(set2)
set2.update(lista3)
print(set2)
# .add() adicionaria a lista como um único valor, .update() descompacta os valores, e joga um a um


# apagar um item - Remove
set2.add(200)
print(set2)
set2.remove(200)
print(set2)

# apagar um item - discard
set2.add(200)
print(set2)
set2.discard(200)
print(set2)
# a única diferença é que o Discard não da erro caso o item não exista


# apagar primeiro item - pop
print(set2)
set2.pop()
print(set2)

set3 = set(range(1, 10))
print(set3)
set3.pop()
print(set3)


# limpar set
set2.clear()
print(type(set2))
# set2 = {}  # isso é um dicionário!
print(set2)

# laço no set
for i in set3:
    print(i)