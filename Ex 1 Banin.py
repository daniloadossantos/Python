print("""Nome do Projeto: Conversor de números reais para binário \n\nIntegrantes do grupo
Danilo Alves dos Santos - 22210022
Douglas Santos Terrero - 22205828
Manuella Souza Silva - 22206155 
Wilson Clayton Silva de Almeida Junior - 22206084 \n""")

nd = float(input("Dado de entrada = "))

while nd >= 1 or nd <= 0:
    nd = float(input("Dado de entrada entre 0 e 1 = "))

print("\nResultados\n")


def dec_bin_menor(num, bits):
    n_bin = str()
    n_desejado = num*2
    for j in range(bits):
        n_int = int(n_desejado // 1)
        resto = float(n_desejado % 1)
        n_desejado = resto * 2
        n_bin += str(n_int)
    return n_bin


def bin_dec_menor(num, bits):
    n_desejado = num*2
    n_dec = 0
    for j in range(bits):
        n_int = int(n_desejado // 1)
        expo = 2 ** -(j + 1)
        if n_int == 1:
            n_dec += expo
        resto = float(n_desejado % 1)
        n_desejado = resto * 2
    return n_dec


def dec_bin_maior(num, bits):
    n_desejado = num * 2
    lista = []
    for j in range(bits):
        n_int = int(n_desejado // 1)
        resto = float(n_desejado % 1)
        n_desejado = resto * 2
        lista.append(n_int)

    cont = 1
    while lista[-cont] == 1:
        lista[-cont] = 0
        cont += 1
    lista[-cont] = 1

    binario2 = ''.join([str(item) for item in lista])
    return binario2


def bin_dec_maior(num, bits):
    n_desejado = num * 2
    lista = []
    for j in range(bits):
        n_int = int(n_desejado // 1)
        resto = float(n_desejado % 1)
        n_desejado = resto * 2
        lista.append(n_int)

    cont = 1
    while lista[-cont] == 1:
        lista[-cont] = 0
        cont += 1
    lista[-cont] = 1

    n_dec = 0
    for j in range(len(lista)):
        expo = 2 ** -(j + 1)
        if lista[j] == 1:
            n_dec += expo
    return n_dec


for i in range(5, 17):

    binario = dec_bin_menor(nd, i)
    decimal = bin_dec_menor(nd, i)
    err = (nd-decimal)/nd * 100

    binario_maior = dec_bin_maior(nd, i)
    decimal_maior = bin_dec_maior(nd, i)
    err_maior = (decimal_maior - nd) / nd * 100

    print("Com {} bits \nAproximação a menor: 0.{} -> {} com erro = {:.3f}%".format(i, binario, decimal, err))
    print("Aproximação a maior: 0.{} -> {} com erro = {:.3f}% \n".format(binario_maior, decimal_maior, err_maior))
