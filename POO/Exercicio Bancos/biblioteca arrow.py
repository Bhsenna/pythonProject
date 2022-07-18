import arrow

data = arrow.now().format('DD/MM/YYYY')
print(data)

data = arrow.now().format('HH:mm')
print(data)


data = arrow.get(3600 * 24)
print(data)

date_1 = arrow.get('2005-07-24 21:30:00', 'YYYY-MM-DD HH:mm:ss')
date_2 = arrow.get('2022-07-14 16:40:00', 'YYYY-MM-DD HH:mm:ss')
diff = date_2 - date_1
print(difsf)