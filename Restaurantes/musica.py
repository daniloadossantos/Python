class Musica:
    musicas = []

    nome = ''
    artista = ''
    duracao = int

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome.ljust(20)} | {self.artista.ljust(20)} | {self.duracao}'

    def listar_musicas():
        print(f'{"Nome".ljust(20)} | {"Artista".ljust(20)} | Duração (seg)')
        for musica in Musica.musicas:
            print(f'{musica.nome.ljust(20)} | {musica.artista.ljust(20)} | {musica.duracao}')

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

Musica.listar_musicas()


# musica1 = Musica()
# musica1.nome = 'Welcome to the jungle'
# musica1.artista = 'Guns n Roses'
# musica1.duracao = 420
#
# musica2 = Musica()
# musica2.nome = 'Bohemian Rhapsody'
# musica2.artista = 'Queen'
# musica2.duracao = 355
#
# musica3 = Musica()
# musica3.nome = 'Shape of You'
# musica3.artista = 'Ed Sheeran'
# musica3.duracao = 234
#
# print(f'Música: {musica1.nome} - Banda: {musica1.artista} - {musica1.duracao} segundos')