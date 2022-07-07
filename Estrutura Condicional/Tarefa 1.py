nome = input('Informe o seu nome: ').upper()
cargo = input('''Selecione o seu cargo (1-3): 
(1) Professor
(2) Coordenador
(3) Zelador \n''')
sal = int(input('Informe o seu Salário: R$'))
salNovo = sal * 1.1
salBon = salNovo * 0.05

if cargo == '1':
    cargo = 'Professor'
elif cargo == '2':
    cargo = 'Coordenador'
elif cargo == '3':
    cargo = 'Zelador'
else:
    cargo = 'Cargo indisponível'

if 2967 > sal > 1999:
    IRRF = salNovo * 0.075
elif 3938 > sal > 2967:
    IRRF = salNovo * 0.15
elif 4987 > sal > 3938:
    IRRF = salNovo * 0.225
elif sal > 4987:
    IRRF = salNovo * 0.275
else:
    IRRF = 0

salLiq = salNovo + salBon - IRRF

print(f'''Colaborador: {nome}
Cargo: {cargo.upper()}
Salário Novo: R${salNovo:.2f}
Bonificação: R${salBon:.2f}
IRRF: R${IRRF:.2f}
Salário Líquido: R${salLiq:.2f}''')