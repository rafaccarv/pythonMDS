import os
os.system("cls")


  

n1 = 0
n2 = 0
n3 = 0


nome1 = input("Digite o nome do primeiro candidato:")
numero1 = input("Digite o número do primeiro candidato:")

nome2 = input("Digite o nome do segundo candidato:")
numero2 = input("Digite o número do segundo candidato:")

nome3 = input("Digite o nome do terceiro candidato:")
numero3 = input("Digite o número do terceiro candidato:")





print("-"*10 , "PARTICIPANTES" , "-"*10)

print(f"Candidado 1 = {nome1} / Número = {numero1}")
print(f"Candidado 1 = {nome2} / Número = {numero2}")
print(f"Candidado 1 = {nome3} / Número = {numero3}")


for cand in range (10):
    cand = input("Digite o numero do candidato:")
    if cand == numero1:
        print(f"Você votou em {nome1}")
        n1 = n1+1
    elif cand == numero2:
        print(f"Você votou em {nome2}")
        n2 = n2+1
    elif cand == numero3:
        print(f"Você votou em {nome3}")
        n3 = n3+1
    else:
        print("Candidato gay não encotrado. Voto anulado.")



print("="*10 , "TABELA DE VOTOS" , "="*10)


print(f"{nome1} teve {n1} de votos")
print(f"{nome2} teve {n2} de votos")
print(f"{nome3} teve {n3} de votos")



ganhador = max(n1,n2,n3)

if n1 == n2 or n2 == n3 or n2 == n3:
    print("Haveu um impate.")
elif n1 > n2 and n1 > n3:
    print(f"Ganhador: {nome1}") 
elif n2 > n1 and n2 > n3:
    print(f"Ganhador: {nome2}")
elif n3 > n2 and n3 > n1:
    print(f"Ganhador: {nome3}")




