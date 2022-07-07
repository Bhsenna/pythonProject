tupla1 = (3, 2, 4)  # Lista com () em vez de []
tupla2 = (3,)  # Tupla de item único
tupla3 = (8, 10, 12)
print(type(tupla1))
print(len(tupla1))
tupla4 = tupla1 + tupla3  # Cria uma Tupla com os valores das 2 Tuplas
print(tupla4)
tupla1 = tupla1 + tupla3  # Tupla só pode ser alterada com outro Tupla
print(tupla1)