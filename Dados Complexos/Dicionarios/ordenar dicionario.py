from operator import itemgetter

times = {'Palmeiras': 18,
         'Flamengo': 12,
         'Coritiba': 22}

print(times)
timesnovo = sorted(times.items(), key=itemgetter(1), reverse=True)  # itemgetter(1) = valores, itemgetter(0) = chaves
print(timesnovo)
# print(type(timesnovo))

for i, time in enumerate(timesnovo):  # i = número, time = tupla
    # enumerate pega os valores de timesnovo, e coloca como um número (index) seguide pelo valor.
    # enumerate(timesnovo) ---> (0, ('Coritiba', 22))
    print(f'{i + 1} - {time[0]} - {time[1]}')