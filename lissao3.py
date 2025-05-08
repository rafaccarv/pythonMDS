
# exercicio 1

# n1 = float(input("digite um número legal: "))
# n2 = float(input("digite outro numero chato:"))
# multiplicacao = n1*n2
# print("a multiplicação de {n1} * {n2} = ", multiplicacao)

# exercicio 2

# number = float(input("digite um numero pra eu te mostrar o antecesor e sucessor dele pois você não sabe pensar e precisa de uma IA feita por mim: "))
# antecessor = number - 1 
# sucessor = number + 1
# print(f"O sucessor é {sucessor} e o antecessor é {antecessor}")

# exercicio 3

# age = float(input("What year were you born? "))
# age2 = 2025 - age
# print(f"You are {age2} years old")


# PORCENTAGEM

# print("25% de 100 =", 0.25 * 100)
# print("4% de 400=", 0.04 * 400)
# print("99% de 1525=", 0.99 * 1525)








prod = (input("digite o nome do primeiro produto:"))
batatavalor = float(input("digite o valor dele:"))
prod2 = (input("digite o nome do segundo produto:"))
tomatevalor = float(input("digite o valor dele:"))
batatadesc = round(batatavalor - (batatavalor *0.10),2)      
tomatedesc = round(float(tomatevalor - (tomatevalor *0.25)),2)
totaldesc = float(tomatedesc + batatadesc)
total = round(float(batatavalor + tomatevalor),2)

print("")

print("="*15,"CAIXA","="*15)

print(f"{prod} custa R${batatavalor}.    Com desconto {batatadesc}")
print(f"{prod2} custa R${tomatevalor}.   Com desconto {tomatedesc}")

print("")

print("."*13,"TOTAL","."*13)

print(f"O total ficou R${total}. Com desconto ficou R${totaldesc}")