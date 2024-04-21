#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = round((n1+n2)/2, 1)
media_alt= (n1+n2)/2
print("Primeira nota do aluno: {} \nSegunda nota do aluno: {} \nA média entre {} e {} é igual a {}" .format(n1,n2,n1,n2,media))
print("Outra forma de codificar a média entre {} e {} é igual a {:.1f}" .format(n1,n2,media_alt))