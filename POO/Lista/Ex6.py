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
        randint()


nome = input('Escolha um nome:')
tamagochi = BichinhoVirtual(nome, 5, 5, 0)

while tamagochi.idade < 20:
