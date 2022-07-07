from Funções.Lista.Func import getFloat as gF


def pegar():
    nome = input('Insira o nome:\n').strip().capitalize()
    nota = gF(f'Informe a nota de {nome}:\n')
    if nota >= 7:
        sit = 'APROVADO'
    else:
        sit = 'REPROVADO'
    dic[nome] = [nota, sit]


def aprov(nome, nota, sit):
    print('\nAluno -', nome)
    print('Nota -', nota)
    print('Situação -', sit)


dic = {}
while True:
    pegar()
    cont = input('Tem mais algum: (S/N)\n').strip().lower()
    if not cont.startswith('s'):
        break
for i in dic:
    aprov(i, dic[i][0], dic[i][1])