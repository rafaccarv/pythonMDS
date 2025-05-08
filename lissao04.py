       #  ATIVIDADE 1


idade = int(input("Digite sua idade: "))

if idade < 0 or idade > 120:
    print("Idade inválida. Acesso negado.")
elif idade >= 18:
    print("Acesso permitido.")
else:
    print("Acesso negado. Você precisa ter 18 anos ou mais.")

    