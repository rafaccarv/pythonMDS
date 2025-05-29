import os
os.system("cls")
borracha = 1.20
lapis = 1.45
caneta = 2.30
carrinho = 0
print("""
DIGITE:
      
1 - COMPRAR UM MATERIAL

2 - MOSTRAR SALDO DO CARRINHO

3 - FINALIZAR COMPRA

4 - SAI DO PROGRAMA

""")
def Comprar():
    global carrinho
    print("ESCOLHA UM ITEM PRA COMPRAR:")
    print("1 - Borracha = R$1.20")
    print("2 - LÁPIS = R$1.45 ")
    print("3 - CANETA = R$2.30")
    
    escolha = int(input("Digite o número do item pra comprar:"))
    
    if escolha == 1:
        boraxa = int(input("Quantas borrachas gostaria de comprar?:"))
        if boraxa > 1:
            print(f"{boraxa} BORRACHAS FORAM ADICIONADAS AO CARRINHO.")
            carrinho = carrinho + boraxa*borracha
        elif boraxa == 1:
            carrinho = carrinho + borracha
    elif escolha == 2:
        lapui = int(input("Quantos lápis gostaria de levar?:"))
        if lapui > 1:
            print(f"{lapui} FORAM ADICIONADOS AO CARRINHO")
            carrinho = carrinho + lapis*lapui
        elif lapui == 1:
            ("1 lápis foi adicionado ao carrinho:")
            carrinho = carrinho + lapis
    elif escolha == 3:
        canuet = int(input("Quantas canetas gostaria de levar?:"))
        if canuet > 1:
            print(f"{canuet} FORAM ADICIONADAS AO CARRINHO.")
            carrinho = carrinho + caneta*canuet
        elif canuet == 1:
            print("1 CANETA FOI ADICIONADA AO CARRINHO.")
            carrinho = carrinho + caneta
    else:
        print("PRODUTO NÃO ENCONTRADO.")
def SaldoCarrinho():
    print(f"Você já adicionou R${carrinho:.2f} ao seu carrinho")
def FinalizarCarrinho():
    print(f"SUA COMPRA DEU R${carrinho:.2f}.")
    finalizar = "n" 
    while finalizar == 'n':
        parcela =  int(input("Quantas vezes gostaria de parcelar? (até 12x): "))

        for i in range(1,parcela+1):
            print(f"PARCELA {i}-> {carrinho/parcela:.2f} ")

        finalizar = input("DESEJA CONFIRMAR A PARCELA?(S/N) ").lower()
        
        if finalizar == "s":
            print("PAGAMENTO EFETUADO! ") 
cmc = 0
while cmc != 4:
    cmc = int(input("O que deseja realizar?:"))

    if cmc == 1:
        Comprar()
    elif cmc == 2:
        SaldoCarrinho()
    elif cmc == 3:
        FinalizarCarrinho()
    elif cmc == 4:
        print("Programa finalizado.")
    else:
        ("Códgo inválido.")