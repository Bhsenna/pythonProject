from Funções.Lista.Func import getInt
from random import randint


class BichinhoVirtual:
    def __init__(self, nome: str, fome: int, saude: int, idade: int):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.humor = (self.fome + self.saude) / 2

    def alterar(self, novo_nome: str, nova_fome: int, nova_saude: int, nova_idade: int):
        print(f'Nome alterado de {self.nome} para {novo_nome}')
        self.nome = novo_nome
        print(f'Fome alterada de {self.fome} para {nova_fome}')
        self.fome = nova_fome
        print(f'Saúde alterada de {self.saude} para {nova_saude}')
        self.saude = nova_saude
        self.humor = (self.fome + self.saude) / 2
        print(f'Idade alterada de {self.idade} para {nova_idade}')
        self.idade = nova_idade

    def mostrar(self):
        print(f'Nome: {self.nome}')
        print(f'Fome: {self.fome}')
        print(f'Saúde: {self.saude}')
        print(f'Idade: {self.idade}')
        print(f'Humor: {self.humor}')

    def alimentar(self):
        print(f'{nome} foi alimentado!')
        self.fome += 1
        self.saude += 1
        satisfacao = randint(0, 6)
        if satisfacao == 0:
            print(f'{nome} odiou comida!')
            self.humor -= 2
        elif satisfacao < 3:
            print(f'{nome} não gostou da comida!')
            self.humor -= 1
        elif satisfacao == 3:
            print(f'{nome} não se importou muito com a comida!')
        elif satisfacao < 6:
            print(f'{nome} gostou comida!')
            self.humor += 1
        else:
            print(f'{nome} amou a comida!')
            self.humor += 2

    def brincar(self):
        print(f'Você brincou com {nome}!')
        self.humor += 1
        self.saude -= 1


nome = input('Escolha um nome:')
tamagochi = BichinhoVirtual(nome, 5, 5, 0)
idade_max = randint(7, 25)

while tamagochi.idade < idade_max and tamagochi.saude > 0:
