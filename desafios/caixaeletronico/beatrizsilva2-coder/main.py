print("Bem- vindo ao caixa eletrônico!")
usuário = input("Digite seu nome: ")
saldo_inicial = float(input("Digite o saldo da conta: R$ "))

print("Menu: "
    "1. Sacar"   
     " 2. Depositar")
opção = int(input("Digite a opção desejada: "))
if opção == 1:
    saque = float(input("Digite o valor que desejar sacar: R$ "))
    if saque > saldo_inicial:
        print ("Saldo insuficiente!")
    else:
        saldo_final = saldo_inicial - saque
        print(f"Usuário: {usuário}")
        print(f"Saldo inicial: R$ {saldo_inicial: .2f}")
        print(f"Valor do saque: R$ {saque: .2f}")
        print(f"Saldo final: R$ {saldo_final: .2f}")

elif opção == 2:
    valor_depósito = float(input(" Digite o valor que deseja depositar: R$ "))
    saldo_final = saldo_inicial + valor_depósito
    print(f"Usuário: {usuário}")
    print(f"Saldo  inicial: R$ {saldo_inicial: .2f}")
    print(f"Valor do déposito: R$ {valor_depósito: .2f}")
    print(f"Saldo final: R$ {saldo_final: .2f}")

else: print("Opção invalida!")

print("Obrigado por usar o caixa eletrõnico!")