# altura = float(input("Informe sua altura em METROS (Ex: 1,70m)  : ").replace("," , "."))
# peso = float(input("Informe seu peso em KG (Ex: 70kg)   : ").replace("," , "."))
# imc = peso/(altura*altura)
# print(f"Seu IMC é {imc:.1f}")
# if imc < 17 :
#     print("Você está muito abaixo do peso. Procure um médico IMEDIATAMENTE!")
# elif imc < 18.49:
#     print("Você está abaixo do peso. Procure um médico!") 
# elif imc < 24.99:
#     print("Você está no peso normal.")
# elif imc < 29.99:
#     print("Você está acima do peso. Procure um médico!")
# elif imc < 34.99:
#     print("Você está na obesidade Ⅰ. Procure um médico IMEDIATAMENTE!")
# elif imc < 39.99:
#     print("Você está na obesidade Ⅱ. Procure um médico IMEDIATAMENTE!")
# else:
#     print("Você está na obesidade Ⅲ. Procure um médico IMEDIATAMENTE!")



def calcular_imc(peso, altura):
    return peso / (altura * altura)

def classificar_imc(imc):
    if imc < 17:
        return "Muito abaixo do peso"
    elif imc < 18.49:
        return "Abaixo do peso"
    elif imc < 24.99:
        return "Peso normal"
    elif imc < 29.99:
        return "Acima do peso"
    elif imc < 34.99:
        return "Obesidade I"
    elif imc < 39.99:
        return "Obesidade II"
    else:
        return "Obesidade III"

def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor <= 0:
                print("Por favor, digite um valor positivo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, insira um número válido.")

def main():
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("     🔍 CALCULADORA DE ÍNDICE DE MASSA CORPORAL")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

    print("Vamos calcular seu IMC? É rápido e fácil!\n")
    
    peso = obter_valor("Informe seu peso em kg (Ex: 65.5): ")
    altura = obter_valor("Informe sua altura em metros (Ex: 1.70): ")

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print("\n📊 Calculando...\n")
    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")

    if "Obesidade" in classificacao or "abaixo" in classificacao.lower():
        print("⚠️ Recomendação: Consulte um médico ou nutricionista!")
    else:
        print("✅ Você está dentro da faixa de peso normal. Continue cuidando da sua saúde!")

    print("\nObrigado por usar nossa Calculadora de IMC! ❤️\n")

# Executar o programa
if __name__ == "__main__":
    main()