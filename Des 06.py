#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input("Digite o numero: "))
print("O dobro de {} é {}. \nO triplo é {}. \nA sua raiz quadrada é {}." .format(n, (n*2), (n*3), (n**(1/2))))
