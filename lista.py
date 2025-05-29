import os
os.system("cls")

lista = []
lista.append(0)
lista.append("caguei")
lista.append(10)
lista.append("tem que ve cos cara la")

print(lista)

lista.pop(2) #pop remove o elemento pelo número
lista.remove("caguei")#"remove" remove pelo valor do elemento


print(lista)

for i in range(len(lista)):
    print(lista[i])

#para alterar elemento da lista finja que o elemento é uma nova variavel
lista[1] = "sim"    

#limpar a lista inteira
lista.clear()