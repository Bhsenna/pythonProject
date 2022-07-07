from operator import itemgetter
nomes = open('nomes.txt', encoding="utf-8", mode="r")
email = open('emails.txt', encoding="utf-8", mode="r")
nomes = nomes.read().splitlines()
email = email.read().splitlines()
dic = {}

for i in range(len(nomes)):
    dic[nomes[i]] = email[i]

alf = sorted(dic.items(), key=itemgetter(0))

for i, j in enumerate(alf):
    print(j[0], j[1], sep=': ')