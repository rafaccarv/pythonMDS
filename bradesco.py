import os
os.system("cls")

encerra = 0

nota100 = 100
nota50 = 50
nota20 = 20
nota10 = 10
nota5 = 5
nota1 = 1

print("""

NOTAS DE =
      
R$100,00  
   
R$50,00

R$20,00

R$10,00

R$5,00
      
R$1,00

""")

numero = 0
ss = 0
ss2 = 0
ss3 = 0
ss4 = 0
ss5 = 0
ss6 = 0
while numero != -1:
    saque = int(input("Digite o valor que quer sacar:"))
    if saque >= 100:
        ss = saque // 100
        print(f"Você sacou {ss} células de 100")




    # if ss >= 50:
    #         ss2 = ss // 50
    #         if ss >= 50:
    #             print(f"Você sacou {ss} células de 100 e {ss2} de 50")
    # if ss2 >=20:
    #             ss3 = ss2 // 20
    #             if ss >= 20:
    #                 print(f"Você sacou {ss} células de 100 e {ss2} de 50 e {ss3} de 20 ")
    # if ss3 > 10:
    #                 ss4 = ss3 // 10
    #                 if ss >= 10:
    #                     print(f"Você sacou {ss} células de 100 e {ss2} de 50 e {ss3} de 20 e {ss4} de 10")
    # if ss4 > 5:
    #                     ss5 = ss4 // 5
    #                     if ss >= 5:
    #                         print(f"Você sacou {ss} células de 100 e {ss2} de 50 e {ss3} de 20 e {ss4} de 10 e {ss5} de 5")
    # if ss5 >= 1:
    #                         ss6 = ss5 // 1
    #                         if ss >= 1:
    #                             print(f"Você sacou {ss} células de 100 e {ss2} de 50 e {ss3} de 20 e {ss4} de 10 e {ss5} de 5 e {ss6} de 1 real")



