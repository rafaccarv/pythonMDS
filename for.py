import os
os.system ("cls")



# for i in range(50):
#     print(i)


# for i in range(-30,16):
#     print(i)



n = int(input("Dize-me um numero entre 1 a 10 e darei-te-ei a tabuada do respectivo numerando:"))

if n > 0 and n < 11:
    for i in range (1,11):
        print(f"{n} x {i} = {n*i}") 
    print("boa, ta melhor de quem colocou um numero maior de 10 e menor que 1 já.")
        

else:
    print("só numero entre 1 a 10, seu cego.")