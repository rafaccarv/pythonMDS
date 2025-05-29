import os
os.system("cls")




precopao = float(input("Digite o preço do pão: "))

for qtdpao in range(1,51):
    print(f" {qtdpao:.2f}- R${precopao*qtdpao:.2f}")

qtdpaocliente = int(input("Quantos pães você vai querer?:"))

if qtdpaocliente > 0 or qtdpaocliente < 51:
        print(f"TOTAL = R${qtdpaocliente*precopao:.2f}")

total = qtdpaocliente*precopao

print(f"O total é de R${total:.2f}\n")

fp = float(input("Qual vai ser a forma de pagamento? NOTA2 NOTA5 NOTA10 OU NOTA50: "))  


if fp >= total:
      cupom = input("Tem algum cupom?:")

      if cupom == "paodeontem":
            total2 = total - (total * 0.10)
            print(f"Seu total é de R${total2:.2f}")
            if total2 < total:
                  print(f"Seu troco é de {fp - total2:.2f}")

else:
      print("Dinheiro insuficiente.")


      
















































