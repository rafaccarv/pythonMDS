import os,random
os.system("cls")
numsj = []
contador=1
while len(numsj)!=10:
    nums = int(input(f"Adicione seu {contador}° número entre 1 e 50:"))
    if nums not in numsj and nums >= 1 and nums <=50:
        numsj.append(nums)
        contador+=1
    else:
        print("Número inválido ou já existente. Perdeu um número")
else:
    print(f"Seus números são: {numsj}")
input("Press enter to continue...")
os.system("cls")
rd = []
sorteados = []
acertos = []
while len(acertos) < len(numsj):
    sorteio = random.randint(1,50)
    if sorteio not in sorteados:
        sorteados.append(sorteio)
        print(f"O número da rodada é {sorteio}")
        if sorteio in numsj:
            acertos.append(sorteio)
            falta = (len(numsj)) - (len(acertos))
            print(f"Você acertou! Números certos: {acertos}\nFaltam {falta} números")
            print(f"Números sorteados: {sorteados}")
            input("Digite enter para continuar")
        else:
            falta = (len(numsj)) - (len(acertos))
            print(f"Não foi dessa vez / Números certos: {acertos}\nFaltam {falta} números")
            print(f"Números sorteados: {sorteados}")
            input("Digite enter para continuar")
    os.system("cls")
print("BINGO")