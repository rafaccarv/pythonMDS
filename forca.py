import os
os.system("cls")
import abc

palavra = input("Digite a PALAVRA:").upper()
palavra = list(palavra)
os.system("cls")

tentativa = input("Fale uma letra:").upper()


def Tente():
    if tentativa in (palavra):
        print(f"Boa! Letra {tentativa} está na palavra!")
        for i in range (len(palavra)):
            i = palavra
        list.pop(i)
        print(f"Letras restantes = {len(palavra)}")

while "ABCDEFGHIJKLMNOPQRSTUVWXYZÇ" in list():
    Tente()





    