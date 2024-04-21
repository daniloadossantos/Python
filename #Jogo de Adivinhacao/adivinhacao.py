print("#################################")
print("Bem-vindo ao jogo de Adivinhação!")
print("#################################")

numero_secreto = 43

numero_usuario = int(input("Digite um número: "))
print("Você digitou {}" .format(numero_usuario))

if(numero_usuario == numero_secreto):
    print("Você acertou!")
else:
    print("Você errou!")

print("Fim do Jogo.")
print("#################################")
