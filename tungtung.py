print("=====================================REAJUSTE DE SALÁRIO AUTOCAR=========================================================")
print(r"""

    #        #        #        #        #        #        #        #        #        #        #        #
 #######  #######  #######  #######  #######  #######  #######  #######  #######  #######  #######  #######
 ## #     ## #     ## #     ## #     ## #     ## #     ## #     ## #     ## #     ## #     ## #     ## #
 #######  #######  #######  #######  #######  #######  #######  #######  #######  #######  #######  #######
    # ##     # ##     # ##     # ##     # ##     # ##     # ##     # ##     # ##     # ##     # ##     # ##
 #######  #######  #######  #######  #######  #######  #######  #######  #######  #######  #######  #######
    #        #        #        #        #        #        #        #        #        #        #        #



""")
      
print("=========================================================================================================================")


salario_atual = float(input("Digite o salário atual do colaborador: "))

if salario_atual <= 2799.99:
    percentual_aumento = 20
elif 2800.00 <= salario_atual <= 6999.99:
    percentual_aumento = 15
elif 7000.00 <= salario_atual <= 14999.99:
    percentual_aumento = 10
else:
    percentual_aumento = 5

valor_aumento = salario_atual * (percentual_aumento / 100)
novo_salario = salario_atual + valor_aumento

print("\n=== RESULTADO DO REAJUSTE ===")
print(f"a. Salário antes do reajuste: R$ {salario_atual:.2f}")
print(f"b. Percentual de aumento aplicado: {percentual_aumento}%")
print(f"c. Valor do aumento: R$ {valor_aumento:.2f}")
print(f"d. Novo salário após o aumento: R$ {novo_salario:.2f}")

