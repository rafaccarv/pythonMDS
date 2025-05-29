import os
os.system("cls")


# É uma função sem parâmentro pois não tem nada dentro dos parenteses, e sem retorno, pois não retorna nada sozinha.

# def Conteudo():
#     print("Oi mundo")

# Conteudo()

#Função com paramentro

# def ExemploParamentro(n1,n2):
#     print(n1+n2)
#     print(n1*n2)

# ExemploParamentro(50,10)

#n1 vale 50 e n2 vale 10

# Função com retorno

# def Retorno():
#     ex = "bom dia"
#     return ex

# print(Retorno())

# teste = Retorno()

# print(teste)


#atividade 1

# def Funcao():
#     print("Bem-vindo ao curso de Python!")

# print(Funcao())


#ativ 2

# def Saudacao():
#     nome = input("Qual seu nome?:")
#     print(f"Olá {nome}")

# print(Saudacao())

# ativ 3

# def Subtracao(n1,n2):
#     n1 = float(input("Fale um número:"))
#     n2 = float(input("Fale outro número:"))
#     result = n1 - n2
#     print(f"{n1} - {n2} = {result}")

# print(Subtracao())

#ativ 3

# def Subtracao(n1,n2):
#     result = n1 - n2
#     return result

# print(Subtracao(3,7))


# ativ 4

# def Fare():
#     conv = float(input("Digite um valor de Fahrenheit:"))
#     result = (conv - 32) / 1.8
#     print(f"Em Celsius isso é {result:.2f}C°")

# print(Fare())


fare = float(input("Digite um número de Fahrenheit:"))

def Formula(fare):
    result = (fare-32) / 1.8
    return result

resumo = Formula(fare)

print (f"Em celsius é: {resumo:.2f}°C")

