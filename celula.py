xiaomi = 2500
iphone = 5000
samsung = 6999.99
























celular = input("Temos Iphone, Xiaomi, Samsung, qual você quer?:").lower()


match celular:
    case "iphone":
        print("Ele custa R$5000,00")
        celular2 = 5000
    case "xiaomi":
        print("Ele custa R$2500,00")
        celular2 = 2500
    case "samsung":
        print("Ele custa R$6999,99")
        celular2 = 6999.99
    case _:
        print("Não temos esse.")   




estado = input("De que estado você é? (Ex: SP):").lower() 


match estado:
    case "sp":
        print("O frete vai ser 10 reais")
        estado2 = 10
    case "mg":
        print("O frete vai ser 15 reais")
        estado2 = 15    
    case "rs":
        print("O frete vai ser 20 reais")
        estado2 = 20
    case _:
        print("O frete vai ser 30 reais")
        estado2 = 30 


print(f"O total é R${estado2 + celular2}")