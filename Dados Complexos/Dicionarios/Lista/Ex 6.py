from operator import itemgetter
users = open('usuarios.txt')
users = users.read().splitlines()
total = 0
dic = {}
j = 0


def conver(byte):
    mb = byte / 1024 ** 2
    return mb


def percen(num):
    per = num / total * 100
    return per


for i in range(len(users)):
    users[i] = users[i].split()
    dic[users[i][0].capitalize()] = conver(int(users[i][1]))
    total += dic[users[i][0].capitalize()]

dic = sorted(dic.items(), key=itemgetter(1), reverse=True)
print("""\33[1;32mACME Inc.   \33[0mUso do espaço em disco pelos usuários
--------------------------------------------------
\33[1;32mNr.  \33[1;33mUsuário        \33[1;35mEspaço utilizado     \33[1;34m% do uso
""")

for i, no in enumerate(dic):
    if i == 0:
        print(f'\33[1;32m{i+1}', (3-len(f'{i+1}'))*' ', f'\33[1;31m{dic[i][0]}', (15 - len(dic[i][0])) * ' ', f'\33[1;35m{dic[i][1]:.2f} MB', (18 - len(f'{dic[i][1]:.2f} MB')) * ' ', f'\33[1;34m{percen(dic[i][1]):.2f}%')
    else:
        print(f'\33[1;32m{i+1}', (3-len(f'{i+1}'))*' ', f'\33[1;33m{dic[i][0]}', (15 - len(dic[i][0])) * ' ', f'\33[1;35m{dic[i][1]:.2f} MB', (18 - len(f'{dic[i][1]:.2f} MB')) * ' ', f'\33[1;34m{percen(dic[i][1]):.2f}%')

print(f'\n\33[0mEspaço total ocupado: \33[1;31m{total:.2f} \33[0mMB')
print(f'\33[0mEspaço médio ocupado: \33[1;31m{(total / len(dic)):.2f} \33[0mMB')