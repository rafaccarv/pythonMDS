# numero = 2 
# while numero < 19:
#     print(numero)
#     numero+=1

# numero = 0 
# while numero > -51:
#     print(numero)
#     numero-=1




















import os
os.system("cls")



print("="*10 , "CADASTRO" , "="*10)
print("")
print("1- NOME / 2- CPF / 3- IDADE ")

c=0

while c != 4:
    c = int(input("Digite a opção desejada:"))

    if c == 1:
        nome = input("Digite seu nome:")
    elif c == 2:
        cpf = input("Digite seu CPF:")
    elif c == 3:
        idade = input("Digte sua idade:")
    elif c == 4:
        print(f"""

SEU CADASTRO:
              
NOME: {nome}
              
IDADE: {idade}
              
CPF: {cpf}


""")
    else:
        print("Código não encontrado. Tente novamente.")





















