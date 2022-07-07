# Número Primo
# Criar um código que recebe um número,
# e diga se ele é primo ou não
# Número primo, tem módulo 0 apenas se dividido
# por 1 ou por ele mesmo

n = int(input('Digite o seu número (natural): '))  # Pega o seu número
a = 2  # Divisor para verificar se seu número é primo

while a < n:  # Mantém o loop enquanto 'a' for menor que 'n'
    if n % a == 0:  # Verifica se alguma das divisões de 'n' por 'a' foi inteiro
        print('Seu número não é Primo')
        break
    a += 1  # Aumenta 'a' em 1 para verificar todos os números possíveis
if n == a:  # verifica se, ao fim do loop, 'a' era igual a 'n'
    print('Seu número é Primo')
elif n == 1:  # verifica se o seu número é 1
    print('Seu número não é Primo')
elif n <= 0:  # verifica se seu número é negativo
    print('Eu falei número natural, seu bobinho')