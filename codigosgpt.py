def verificar_idade():
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 0 or idade > 120:
            print("❌ Idade inválida. Digite um valor entre 0 e 120.")
            
        elif idade >= 18:
            print("✅ Acesso permitido. Bem-vindo!")
            
        else:
            print("🚫 Acesso negado. É necessário ter pelo menos 18 anos.")
            

    except ValueError:
        print("⚠️ Por favor, digite apenas números inteiros.")
         



# def autenticar_usuario():
#     EMAIL_CORRETO = "python@senai.com"
#     SENHA_CORRETA = "12345678"

#     email = input("Digite seu e-mail: ").strip()
#     senha = input("Digite sua senha: ").strip()

#     if email.lower() == EMAIL_CORRETO and senha == SENHA_CORRETA:
#         print("✅ Autenticação realizada com sucesso!")
        
#     else:
#         print("❌ E-mail ou senha incorretos. Verifique e tente novamente.")
        
