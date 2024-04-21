#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
n = int(input("Digite um número para ver sua tabuada: "))
for c in range (1,10+1):
    tabuada=0
    tabuada = n*c
    print("{} x {} = {}" .format(n, c, tabuada))
