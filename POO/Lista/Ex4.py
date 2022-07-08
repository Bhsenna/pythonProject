class BombaCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float):
        self.tipo = tipo_combustivel
        self.valorLitro = valor_litro
        self.quantidade = 11000

    def abastecer_por_valor(self, valor: float):
        quantidade = valor / self.valorLitro
        print(f'Foi adicionado {quantidade:.2f} litros de gasolina ao tanque!')
        self.quantidade -= quantidade

    def abastecer_por_litro(self, quantidade: float):
        preco = quantidade * self.valorLitro
        print(f'Você deve pagar R${preco:.2f} pelos {quantidade} litros!')
        self.quantidade -= quantidade

    def alterar_valor(self, valor: float):
        print(f'Valor alterado com sucesso, de RS{self.valorLitro:.2f} para R${valor:.2f}')
        self.valorLitro = valor

    def alterar_combustivel(self, novo_combustivel: str):
        print(f'Tipo de Combustível alterado com sucesso para {novo_combustivel}')
        self.tipo = novo_combustivel

    def alterar_quantidade_combustivel(self, nova_quantidade):
        print(f'Quantidade de Combustível alterada com sucesso para {nova_quantidade} litros')
        self.quantidade = nova_quantidade


b1 = BombaCombustivel('Etanol', 5.99)
b1.abastecer_por_valor(50)
b1.abastecer_por_litro(5)
b1.alterar_valor(3.50)
b1.abastecer_por_valor(50)
b1.abastecer_por_litro(5)
b1.alterar_combustivel('Diesel')
b1.alterar_quantidade_combustivel(1)