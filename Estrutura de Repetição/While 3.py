# Adaptar o código anterior para que sejam todos os números primos entre 1 e 100
n = 1
while n <= 100:
    a = 2  # Divisor para verificar se seu número é primo
    while a < n:  # Mantém o loop enquanto 'a' for menor que 'n'
        if n % a == 0:  # Verifica se alguma das divisões de 'n' por 'a' foi inteiro
            break
        a += 1  # Aumenta 'a' em 1 para verificar todos os números possíveis
    if n == a:  # verifica se, ao fim do loop, 'a' era igual a 'n'
        print(n)
    n += 1