class Carro:
    def __init__(self, km_por_litro: int):
        self.__consumo = km_por_litro
        self.__tanque = 0

    def acoes(self, acao):
        if acao == '1':
            carro1.__andar(getFloat('Quantos KM deseja andar? '))
        elif acao == '2':
            carro1.__adicionar_gasolina(getFloat('Quantos Litros deseja colocar no tanque? '))
        elif acao == '3':
            carro1.__obter_gasolina()

    def __adicionar_gasolina(self, quantidade_gasolina: float):
        self.__tanque += quantidade_gasolina
        print('Tanque abastecido')

    def __obter_gasolina(self):
        print(f'Quantidade de Gasolina no tanque: {self.__tanque} litros')

    def __andar(self, kilometros: float):
        gasto = kilometros / self.__consumo
        if gasto > self.__tanque:
            print(f'Sua gasolina acaba após {self.__tanque * self.__consumo}km')
            exit()
        else:
            print(f'Você andou {kilometros} km')
            self.__tanque -= gasto


from Funções.Lista.Func import getInt
from Funções.Lista.Func import getFloat
carro1 = Carro(getInt('Consumo (km/litro) do carro: '))
while True:
    carro1.acoes(input('Você deseja:\n[1] Andar com o Carro\n[2] Abastecer o Carro\n[3] Verificar o Tanque\n'))