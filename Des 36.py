vl_casa = 0
sal = 0
anos = 0
prest = 0
limite = 0


vl_casa = float(input("Qual o valor da casa: "))
sal = float(input("Digite o salário: R$ "))
anos = float(input("Em quantos anos deseja pagar: "))

prest = float(vl_casa/(anos*12))
limite = sal*0.3

if prest < limite:
    print("Seu empréstimo foi aprovado. A prestação será no valor de R$ {:.2f}." .format(prest))
else:
    print("Empréstimo reprovado!")

