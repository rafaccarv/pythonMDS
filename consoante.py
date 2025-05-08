

# letter = input("give me a random letter:")

# if letter in "aeiouAEIOU" :
#      print ("vowel")

# else:
#      print("consonant")









# letter = input("give me a random letter:")

# if letter == "A" or letter == "a"  or letter == "E" or letter == "e" or letter == "I" or letter == "i" or letter == "O" or letter == "o" or letter == "U" or letter == "u" :
    
#      print("vowel")

# else:
#      print("consonant")






# letter = input("Give me a random letter: ").strip()

# if len(letter) != 1:
#     print("Please enter exactly one letter.")
# else:
#     if letter.lower() in 'aeiou':
#         print("vowel")
#     else:
#         print("consonant")






try:
    
    letra = input("Dê-me uma letra aleatória: ").strip()

    
    if len(letra) != 1:
        raise ValueError("Você deve inserir exatamente uma letra.")

    
    if not letra.isalpha():
        raise ValueError("Você só pode inserir letras, não números ou símbolos.")

   
    if letra.lower() in 'aeiou':
        print("vogal")
    else:
        print("consoante")


except ValueError as ve:
    print(f"Erro: {ve}")


except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")