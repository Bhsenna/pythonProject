l1 = int(input('Informe o lado 1 do Triângulo: '))
l2 = int(input('Informe o lado 2 do Triângulo: '))
l3 = int(input('Informe o lado 3 do Triângulo: '))

if l1 + l2 < l3 or l2 + l3 < l1 or l1 + l3 < l2:
    print('Isso não é um triângulo!')
elif l1 == l2 == l3:
    print('Você tem um Triângulo Equilátero!')
elif l1 == l2 or l2 == l3 or l1 == l3:
    print('Você tem um Triângulo Isósceles!')
else:
    print('Você tem um Triângulo Escaleno!')

esp1 = l3 // 2
des = l1 - 1
esp2 = 0
while des > 0 and esp1 != 0:
    print(esp1*' ' + "/" + esp2*' ' + "\\")
    des -= 1
    esp1 -= 1
    esp2 += 2
print('/' + l3*'_' + '\\')
# esse desenho == eu não tenho vida
