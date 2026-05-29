produtos = {
    "Arroz": 23.00,
    "Feijão": 8.00,
    "Coca Cola": 15.00,
    "Açúcar": 9.00
}

carrinho = {}
total_compra = 0

print("Bem-vindo ao mercado CODE!")
print("Produtos disponíveis:")

for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")

while True:
    produto = input("\nDigite o nome do produto: ")

    if produto in produtos:
        quantidade = int(input("Digite a quantidade desejada: "))

        if quantidade > 0:
            valor_produto = produtos[produto] * quantidade
            carrinho[produto] = quantidade
            total_compra += valor_produto

            print(f"Produto adicionado: {produto}")
            print(f"Quantidade: {quantidade}")
            print(f"Valor: R$ {valor_produto:.2f}")
        else:
            print("A quantidade deve ser maior que zero.")
    else:
        print("Produto não encontrado.")

    continuar = input("Deseja adicionar mais produtos? (s/n): ")

    if continuar.lower() != "s":
        break

print("\nResumo da compra:")

for produto, quantidade in carrinho.items():
    print(f"{produto} - Quantidade: {quantidade}")

print(f"Total da compra: R$ {total_compra:.2f}")

if total_compra > 100:
    desconto = total_compra * 0.10
    total_final = total_compra - desconto

    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Total com desconto: R$ {total_final:.2f}")
else:
    print("Nenhum desconto aplicado.")
    print(f"Total a pagar: R$ {total_compra:.2f}")

print("Obrigado por comprar conosco!")
print("Volte sempre!")