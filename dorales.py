import os
os.system("cls")


# print("""

# Digite 1 - Converter dólar em Real
# Digite 2 - Converter Real em Dolar
# Digite 3 - Sair 


# """)


# bagui = float(input("Qual opção você quer?:"))

# while bagui != 3:
#     if bagui == 1:
#         emreal = float(input("Quantos dolares você tem?:"))
#         real = emreal / 5.67
#         print(f"Você tem R${real:.2f}")
#     elif bagui == 2:
#         emdola = float(print("Quantos reais você tem?:"))
#         dola = emdola * 5.67
#         print(f"Você tem ${dola}")
#     else:
#         ("Código inválida.")




print("""
Digite 1 – Converter dólar em Real
Digite 2 – Converter Real em Dolar
Digite 3 – Sair 
""")


def dolar_real():
    dolarpreal = d * 5.67
    return dolarpreal

def real_dolar():
    realpdolar = 5.67 / d
    return realpdolar





cmc = 0


while cmc != 3:
    cmc = int(input("Qual opção você quer?:"))
    if cmc == 1:
        d = float(input("Quantos dolares você tem?:"))
        print(f"Você tem R${dolar_real():.2f}")
    elif cmc == 2:
        d = float(input("Quantos reais você tem?:"))
        print(f"Você tem ${real_dolar():.2f}")
    elif cmc == 3:
        print("Pogama incerado.")
    else:
        print("um numero da lysta.")


























