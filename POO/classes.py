# classe para um veículo
from Funções.Lista.Func import getInt


class Veiculo:
    # cor, porta, marca, modelo, ano
    def __init__(self, cor, porta, marca, modelo, ano):
        self.cor = cor
        self.porta = porta
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __repr__(self):
        return repr(f'{self.marca} - {self.modelo} - {self.porta} portas - {self.cor} - {self.ano}')

    def ligar(self):
        print(f'Vroom Vroom {self.modelo} foi ligado')
        print('\33[1;3mComece a correr\33[0m')

    def desligar(self):
        print(f"Vroom Vroom do {self.modelo} acabou")


veiculos = []

for _ in range(2):
    cor = input('Informe a cor: ')
    porta = getInt('Informe a quantidade de portas: ')
    marca = input('Informe a marca: ')
    modelo = input('Informe o modelo: ')
    ano = input('Informe o ano: ')
    cadastro = Veiculo(cor, porta, marca, modelo, ano)
    veiculos.append(cadastro)

for i in veiculos:
    print(i)