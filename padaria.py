import os
os.system("cls")




precopao = float(input("Digite o preço do pão: "))

for qtdpao in range(1,51):
    print(f" {qtdpao}- R${precopao*qtdpao:.2f}")

qtdpaocliente = int(input("Quantos pães você vai querer?:"))

if qtdpaocliente > 0 or qtdpaocliente < 51:
        print(f"TOTAL = R${qtdpaocliente*precopao}")

total = qtdpaocliente*precopao

fp = float(input("Qual vai ser a forma de pagamento? NOTA2 NOTA5 NOTA10 OU NOTA50: "))                # cupom = input("Tem algum cupom?:")

if fp == total:
      print("Obrigado, tenha um otimo dia")
    
elif total > fp :
      print(f"Faltam R${total - fp}")


elif fp > total:
      print(f"Seu troco é de R${fp - total}")



