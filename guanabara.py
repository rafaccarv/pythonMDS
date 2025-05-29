import os
os.system("cls")
import random 
print("="*10 , "ÁREA DA MATEMÁTICA" , "="*10)
print("""
DIGITE:
1- Para somar.
2- Para multiplicar.
3- Ver qual número é maior.
4- Para ver novos números.
5- Sair do programa.     
""")
fn = int(input("Digite o primeiro número:"))
sn = int(input("Digite o segundo número:"))
sla = 0
while sla != 5:
    pogama = int(input("Qual opção você quer?: "))
    if pogama == 1:
        print(f"{fn} + {sn} = {fn + sn}")
    elif pogama == 2:
        print(f"{fn} x {sn} = {fn*sn}")
    elif pogama == 3:
        max = max(fn,sn)
        print(f"O maior número é {max}")
    elif pogama == 4:
        fn = int(input("Digite um novo número:"))
        sn = int(input("Mais outro:"))
else:
    print("programa encerrado.")
