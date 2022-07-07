class Macaco:
    def __init__(self, nome: str):
        self.nome = nome
        self.bucho = []

    def comer(self, comida):
        self.bucho.append(comida)

    def ver_bucho(self):
        print(self.bucho)

    def digerir(self):
        self.bucho.clear()


macacos = {}
for _ in range(3):
    nome = input('Informe o nome do Macaco: ')
    macaco = Macaco(nome)
    macacos[f'{nome}'] = macaco

while True:
    print('Deseja interagir com ', end='')
    a = 1
    for i in macacos:
        if a < len(macacos):
            print(i, end=' ou ')
            a += 1
        else:
            interagente = input(f'{i}\n')
    if interagente not in macacos:
        continue
    acao = input('Desejas [1] Alimentar, [2] Ver Bucho, [3] Digerir?\n')
    if acao == '1':
        comida = input('O que você dara a ele?\n')
        if comida in macacos:
            print('NÃO FAÇA UM MACACO COMER UM MACACO!')
            macacos[f'{interagente}'].comer(comida)
            macacos.pop(comida)
        else:
            macacos[f'{interagente}'].comer(comida)
    elif acao == '2':
        macacos[f'{interagente}'].ver_bucho()
    elif acao == '3':
        macacos[f'{interagente}'].digerir()
    else:
        continue
    if input('Deseja parar?\n').lower().startswith('s'):
        break