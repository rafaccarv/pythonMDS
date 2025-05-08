            #    ATIVIDADE 2


email_correto = "python@senai.com"
senha_correta = "12345678"

email = input("Digite seu e-mail: ")
senha = input("Digite sua senha: ")

if email == email_correto and senha == senha_correta:
    print("USUÁRIO AUTENTICADO")
else:
    print("USUÁRIO ou senha Inválidos!")