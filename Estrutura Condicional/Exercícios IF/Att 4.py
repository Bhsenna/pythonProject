# Elabore um algoritmo que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de pagamento.
# Utilize os códigos da tabela a seguir para ler qual a condição de pagamento
# escolhida e efetuar o cálculo adequado.

preço = float(input('Informe o preço de etiqueta do produto desejado: R$'))
forma = int(input('''Selecione a forma de pagamento:
(1) À vista (dinheiro ou cheque)
(2) À vista (cartão de crédito)
(3) Em duas vezes (sem juros)
(4) Em duas vezes (juros 10%)\n'''))

if forma == 1:
    print(f'Você irá pagar R${(preço - (preço * 0.10)):.2f}')
elif forma == 2:
    print(f'Você irá pagar R${(preço - (preço * 0.15)):.2f}')
elif forma == 3:
    print(f'Você irá pagar R${(preço / 2):.2f} duas vezes. Total: R${(preço):.2f}')
elif forma == 4:
    print(f'Você irá pagar R${((preço + (preço * 0.1)) / 2):.2f} dua vezes. Total: R${(preço + (preço * 0.1)):.2f}')
else:
    print('Forma de pagamento inválida')