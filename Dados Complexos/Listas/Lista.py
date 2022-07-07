# lista = [1, 2, 1.6, 4]
#
# # lista.append(True)
# lista2 = [3, 5, 8]
# # lista += lista2  # conteúdo da lista no final - não funciona com tupla ou dicionários
# # lista.append(lista2)  # lista dentro da lista
# lista.extend(lista2)  # conteúdo da lista no final - funciona com tupla ou dicionários
# print(lista)
#
# lista.insert(3, 'Hazime')  # Primeiro a posição, depois o item - adiciona o item na posição, a bota o resto 1 pro lado
# # se a posição for maior que o tamanho total da lista, o item será colocado no final
# lista.insert(3, 'Hazime')
# print(lista)
# lista.insert(len(lista), 'Haha')  # len(lista) coloca na última posição (só usa .append que é mais facil), -1 coloca na penúltima
# print(lista)
#
# lista.remove('Hazime')  # Remove o PRIMEIRO item da lista que seja igual ao valor dentro do .remove()
# # Remover todos os valores iguais a 'Hazime' precisaria de um loop com for
# print(lista)
#
# lista.pop()  # Apaga o ultimo item da lista quando vazio, coloque um valor para especificar a posição apagada
# print(lista)
# lista.pop(5)  # Se usado dentro de uma variável/print, armazena o valor apagado
# print(lista)
# lista.pop(6)
# print(lista)
#
# lista.clear()  # mesma coisa que 'lista = []'
# del lista[:]  # deleta as posições especificadas - '[:]' significa 'tudo'
# print(lista)

lista3 = ['jonas', 'carlos', 'joaquim', 'simon', 'garfunkel']
lista3.sort()  # Organiza a lista em ordem alfabética
print(lista3)
lista3.sort(reverse=True)  # Organiza a lista em ordem contra-alfabética
print(lista3)
#  Ordem alfabética: Especiais, Números, Letras Maiúsculas, Letras Minúsculas
lista4 = [3,5,2,4]
lista4.sort()
print(lista4)

lista5 = ['ar', 'r', 'a', 'r', 'a']
print(lista5.count('a'))  # conta quantas vezes um item aparece dentro dessa lista
lista5.reverse()  # inverte a ordem da lista
print(lista5)

#
# append
# extend
# insert
# remove
# pop
# clear
# sort
# count