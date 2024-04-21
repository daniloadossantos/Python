#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
dist = float(input("Digite a distância em metros: "))
km = dist/1000
hm = dist/100
dam = dist/10
dm = dist*10
cm = dist*100
mm = dist*1000
print("A medida de {:.1f}m corresponde a: \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm" .format(dist, km, hm, dam, dm, cm, mm))