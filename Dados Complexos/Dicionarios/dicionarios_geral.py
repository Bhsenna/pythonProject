# Declarar um dicionário
# {chave 1 : valor 1, chave 2 : valor, ........, chave n : valor n}

dic = {'jonas': 'jonasreiter@hotmail.com',
       'susan': 'susan.reiter@hotmail.com',
       'Professora': 'contato@reiter.page'}

# chave : valor

# ---------------------------------------------------------------------

# imprimir o dicionario completo
# print(dic)

# Imprimir apenas um valor do dicionario
# print(dic['susan'])
# print(dic.get('susan'))
# print(dic.get('João', 'não existe'))
# print(dic.get('Hazime', 'Não tem'))

# ---------------------------------------------------------------------

# adicionar um item ao dicionaro
# dic['Acesso'] = 'entra21@acesso.com.br'
# print(dic)
# dic['Hazime'] = 'bhsenna@gmail.com'
# print(dic)
# print(dic['Acesso'])

# ---------------------------------------------------------------------

# alterar um valor do dicionario forma 1
# dic['susan'] = 'susan@gmail.com.br'
# print(dic)

# alterar um valor do dicionario forma 2
# dic.update({'jonas': 'jonas123@hotmail.com', 'susan': 'susan@gmail.com.br})
# print(dic)

# ---------------------------------------------------------------------

# alterar o nome da chave forma 1
# dic['Professaura'] = dic.pop('Professora')
# print(dic)

# alterar o nome da chave forma 2
# dic['Professora'] = dic['Professaura']
# del dic['Professaura']
# print(dic)

# ---------------------------------------------------------------------

# imprimir todas as chaves de uma vez
# print(dic.keys())

# imprimir todos os valores
# print(dic.values())

# percorrer todas as chaves no laço
# for i in dic:
#     print(i)

# percorrer todos os valores
# for i in dic:
#     print(dic[i])

# percorrer o dicionario completo
# for k, v in dic.items():  # key, value
#     print(f'{k}------{v}')

# deletar um item específico
# dic.pop('susan')
# print(dic.values())


# deletar o último item do dicionário
# dic.popitem()
# print(dic.values())


# Verificar se um item está nas chaver dicionário
# if 'casimiro' in dic:
#     print('encontrei')
# else:
#     print('Nops')

# Verificas se um item está nos valores do dicionário
# if 'jonasreiter@hotmail.com' in dic.values():
#     print('encontrei')
# else:
#     print('Nops')
# Criar um dicionario a partir de uma lista
# chaves = ['a', 'b', 'c']
# valor = 0
# novo_dic = dict.fromkeys(chaves, valor)
# print(novo_dic)
# {'a': 0, 'b': 0, 'c': 0}

# Criando dicionario a partir de 2 listas
lista1 = ['jonas', 'raul', 'stefan']
lista2 = [30, 30, 50]
dic3 = {}
for i in range(len(lista1)):
    dic3[lista1[i]] = lista2[i]
print(dic3)

# juntar 2 dicionários
dic4 = {**dic, **dic3}
print(dic4)

# limpar o dicionario
dic.clear()
print(dic)