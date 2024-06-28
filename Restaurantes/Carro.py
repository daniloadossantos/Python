class Carro:

    carros = []

    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = str(ano)
        Carro.carros.append(self)

    def __str__(self):
        return f'Modelo: {self.modelo.ljust(20)} | Marca: {self.marca}'

    def listar_carros():
        print(f'{"Marca".ljust(20)} | {"Modelo".ljust(20)} | {"Ano".ljust(20)} | Cor')
        for carro in Carro.carros:
            print(f'{carro.marca.ljust(20)} | {carro.modelo.ljust(20)} | {carro.ano.ljust(20)} | {carro.cor}')


carro1 = Carro('GM', 'Corsa', 'Preto', 1990)
carro2 = Carro('VW', 'Gol', 'Branco', 2008)
carro3 = Carro('Ford', 'Ka', 'Azul', 1999)

Carro.listar_carros()