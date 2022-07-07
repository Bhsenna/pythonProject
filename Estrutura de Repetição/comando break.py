contador = 1
total = 0

while True:
    total = 2**contador
    print(total)
    contador += 1
    if total > 2000:
        break