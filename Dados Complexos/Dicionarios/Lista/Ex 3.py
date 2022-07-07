from datetime import date
from Funções.Lista.Func import getFloat as gF
from Funções.Lista.Func import getInt as gI
dic = {}


def pegar(j):
    nome = input('\nInsira o nome:\n').strip().capitalize()
    while True:
        gen = input('Genero: (M/F/X)\n').strip().upper()
        if gen.startswith(('M', 'F', 'X')):
            break
    ano = input('Ano de Nascimento: (dd/mm/aaaa)\n').strip()
    ano = date(int(ano[6:10]), int(ano[3:5]), int(ano[0:2]))
    idade = date.today().year - ano.year - ((date.today().month, date.today().day) < (ano.month, ano.day))
    cart = input('Carteira de Trabalho:\n').strip()
    if cart != '0':
        cont = input('Ano de Contratação: (dd/mm/aaaa)\n').strip()
        sal = gF('Salário:\nR$')
        if gen == 'M':
            apo = '65 anos'
        elif gen == 'F':
            apo = '62 anos'
        else:
            apo = '65 anos'
        dic[j] = {'Nome': nome, 'Gênero': gen, 'Idade': f'{idade} anos', 'CTPS': cart, 'Ano de Contratação': cont, 'Salário': f'R${sal:.2f}', 'Aposentadoria': apo}
    else:
        dic[j] = {'Nome': nome, 'Gênero': gen, 'Idade': f'{idade} anos', 'CTPS': cart}


n = gI('Quantas pessoas deseja cadastrar?\n')
for i in range(n):
    pegar(i)

for i in dic:
    for j in dic[i]:
        print(j, dic[i][j], sep=': ')
    print()