import os 
os.system("cls")

print("""
1 - Adicione um produto na lista.
2 - Remova um produto da lista.
3 - Exclua todos os produtos da lista.
4 - Saia do programa.
5 - Exiba os produtos da lista.
""")

produto = ""
lista = []

def PriOp():
    global lista
    global produto
    produto = input("Adicione algo na lista:")
    lista.append(produto)

def SecOp():
    global lista
    global produto
    produto = input("Escreva o que você quer remover (o conteúdo da mensagem):")
    lista.remove(produto)

def Tercop():
    global lista
    global produto
    lista.clear()

def QuintOp():
        global produto
        global lista
        print(produto)


cmc = 0


while cmc != 4:
    cmc = int(input("Qual opção você quer?:"))
    if cmc==1:
        PriOp()
    elif cmc==2:
        SecOp()
    elif cmc==3:
        Tercop()
    elif cmc==4:
        print("programa enserrado.")
    elif cmc==5:
        QuintOp()
    else:
        ("cod não encontrado.")