import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")


# Desenhos pedra papel tesoura



# papel = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

pedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


# tesoura = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """






import random







print("_"*17 , "JOGUE PAPEL, PEDRA OU TESOURA" , "_"*17)
print("")
print("")


robo = random.randint(1,3) 

algo = input("Qual você vai jogar?:").lower()





match robo:
    case 1:
        esc_rob = "tesoura"
        print("O robô escolheu: TESOURA") 
    case 2:
        esc_rob = "papel"
        print("O robô escolheu: PAPEL")
    case 3:
        esc_rob = "pedra"
        print("O robô escolheu: PEDRA")


match (algo, esc_rob):

    case (j, r) if j == r:
        print("Empate!")
    case ("pedra", "tesoura"):
        print("Você venceu!")
    case ("tesoura", "papel"):
        print("Você venceu!")
    case ("papel", "pedra"):
        print("Você venceu!")
    case ("tesoura", "pedra"):
        print("Você perdeu!")
    case ("papel", "tesoura"):
        print("Você perdeu!")
    case ("pedra", "papel"):
        print("Você perdeu!")
    case _:
        print("Jogada inválida.")



