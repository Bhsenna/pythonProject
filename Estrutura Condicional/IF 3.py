n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# if n1 >= n3:
#     n1, n3 = n3, n1
# if n2 <= n1:
#     n2, n1 = n1, n2
# if n2 >= n3:
#     n2, n3 = n3, n2
#
# print(f'Crescente: {n1}, {n2}, {n3}')
# print(f'Decrescente: {n3}, {n2}, {n1}')

num = [n1, n2, n3]
num2 = num

num.sort()
num2.sort(reverse=True)

print(f'Crescente: {num}')
print(f'Decrescente: {num2}')

print("\nJoilson salva tudo e todos. God d+")