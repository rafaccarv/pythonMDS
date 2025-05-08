n1 = float(input("Enter the student's first grade: ").replace("," , "."))
n2 = float(input("Enter the student's second grade: ").replace("," , "."))
m = (n1 + n2) / 2

print(f"Your average is {m}")

if m <= 5:
    print("FAILED, BRUH.")

elif m <= 7:
    print("In recovery, lucky lucky.")

elif m > 7:
    print("Passed, smartass.")

# o .replace tem de estar dentro do input, como (input("oi, tudo bem?:").replace("," , "."))

bv = (input("oi, tudo bem?:\n").replace("," , "."))

print(f"\n{bv} {bv} {bv} {bv} {bv} {bv} ahhhhhh calaboca kkkkkkkkkkkkhkkkkkkjjk lixinho")