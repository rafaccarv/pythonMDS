import os
os.system("cls")



n = 0
maior = 0



for i in range(5): 
    n = int(input("Digite um numero: "))
    if i == 0 or n > maior: 
        maior = n

print(f"O maior número é: {maior}")


