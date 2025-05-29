import os
os.system("cls")

# soma = 0
# lista = [] 

# for i in range (10):
#     numero = float(input("Digite um número:")) 
#     lista.append(numero)
#     soma += numero
    
# print("Soma =" , soma)
    

lista = []
dst = 0 
nm = input("Digite o nome do(a) atreta:").upper()
while nm != "":
    for i in range (1,6):
        numero = float(input(f"Digite a distância do {i}° salto:"))
        lista.append(numero)
        dst = numero + dst   

    else:
        final = dst / 5
        print(f"{i}° salto = {lista[0
                                    ]}")
        print(f"A média dos saltos de {nm} é: {final}")

print("Programa encerrado por falta de atletas.")