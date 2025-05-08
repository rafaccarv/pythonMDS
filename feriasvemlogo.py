numero = int(input("Digite um número de 1 a 7 então dar-te-ei o dia da semana correspondente ao tal:"))

match numero:
    case 1: 
        print("Segunda")

    case 2:
        print("Terça")
       
    case 3: 
        print("Quarta")
        
    case 4: 
        print("Quinta")
    
    case 5: 
        print("Sexta")
    
    case 6: 
        print("Sabado")
    
    case 7: 
        print("Domingo")
    
    case _: 
        print("Infortúnio no engenho do sistema. Introduzi um algarismo de 1 a 7, e dar-te-ei a conhecer o dia da semana que à dita cifra corresponde.")
