from Avaliacao import Avaliacao
class Restaurante:
    restaurantes = []

    # construtor
    def __init__(self, nome, categoria, capacidade):
        self.nome = nome
        self.categoria = categoria.upper()
        self._ativo = False #atributo PROTEGIDO
        self.capacidade = str(capacidade)
        self._avaliacao = []
        Restaurante.restaurantes.append(self) #toda vez cria um objeto e insere na lista restaurantes

    #self => referencia da instancia atual que estamos utilizando no momento
    def __str__(self):
        return f'{self.nome.ljust(20)}'

    @classmethod #BOA PRÁTICA - para indicar que é um metodo da classe
    def listar_restaurantes(cls):
        print(f'{"Nome".ljust(20)} | {"Categoria".ljust(20)} | {"Capacidade".ljust(20)} | {"Nota".ljust(19)} '
              f'| Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | '
                  f'{restaurante.capacidade.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)}| {restaurante.ativo}')

    def alternar_estado(self):
        self._ativo = not self._ativo #para trocar o estado do Ativo

    #@property
    #def nota_avaliacao(self):
    #    return '★' * self._nota_avaliacao

    @property #para modificar como o atributo será lido
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao) #para cada avaliacao dentro do ._avaliacao, pega a ._nota
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas/quantidade_notas, 1)
        return media

#restaurante_praca = Restaurante('Bistrô', 'Italiana', 100, 5)
#restaurante_praca.alternar_estado()

#restaurante_pizza = Restaurante('Pizza Place', 'Fast Food', 55, 3)

#vars => utilizado para imprimir os atributos da classe
# print(vars(restaurante_praca))
# print(vars(restaurante_pizza))

# print(f'{"Nome".ljust(20)} | {"Categoria".ljust(20)}')
# print(restaurante_praca)
# print(restaurante_pizza)

#Restaurante.listar_restaurantes()


