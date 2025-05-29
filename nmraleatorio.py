
import os
os.system("cls")


# import random



# botnumber = random.randint(1,10)
# urnumber = 0 

# while botnumber != urnumber:
#     urnumber = int(input("Digite um numero:"))
#     if botnumber != urnumber:
#         print(f"O robô escolheu {botnumber}, você errou.")
#     else:
#         print("Boa!")




# ATIVIDADE 2

# senha = 1505
# encerramento = 9999
# persona = 0



# while senha != persona or encerramento != persona:
#     persona = int(input("Digite sua senha:"))
#     if senha == persona:
#         print("Senha correta!")
#     elif senha != persona and encerramento == persona:
#         print("Sessão encerrada")
#     elif senha != persona:
#         print("Senha incorreta.")















print("""

===========BANCO GRILLAL===========
      
1-  DEPÓSITO

2- SAQUE

3- MOSTRA O SALDO DA CONTA
      
4-SAI DO PROGRAMA


""")



bgl = 0
saldo = 0 

while bgl != 4:
    bgl = int(input("Digite  opção desejada:"))
    if bgl == 1:
        deposito = float(input("Digite o valor do deposito:"))
        print(f"Você depositou {deposito}")
        saldo = saldo + deposito

    elif bgl == 2:
        saque = float(input(f"Quando você quer sacar?:"))
        if saque <=deposito:
            print(f"Você sacou {saque}")
            saldo = saldo - saque 
        else:
            ("Saldo insuficiente para este saque.") 

    elif bgl == 3:
        print(f"Seu saldo é de R${saldo}.")

    else:
        print("Código não encontrado")






































    
    