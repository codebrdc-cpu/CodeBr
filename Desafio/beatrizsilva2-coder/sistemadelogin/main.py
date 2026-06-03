# Entrada De Dados
senha = input("Digite a senha: ")
senha_correta = "1234"

# Processamento

tentativas = 4
while tentativas > 0:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso permitido")
        break
    else:
        tentativas -= 1
        print(f"Acesso negado. Tem {tentativas} restante")
        if tentativas == 0:
            print("Acesso bloqueado, esgostou as tentativas")