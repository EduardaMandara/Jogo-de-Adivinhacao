print ("Jogo de Adivinhação!")

numero_secreto = 7
chute_str = input("Digite um número: ")
chute = int(chute_str) #conversão de str para int.

print("Você digitou", chute_str)

if (numero_secreto == chute):
  print("Você acertou!")
else:
  print("Você errou!")