from restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet', 100)
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana', 50)
restaurante_japones = Restaurante('Sushi Food', 'Japonesa', 45)

restaurante_praca.receber_avaliacao('Guilherme', 10)
restaurante_praca.receber_avaliacao('Talita', 4)
restaurante_praca.receber_avaliacao('João', 4)
restaurante_mexicano.alternar_estado()
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()