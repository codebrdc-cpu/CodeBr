#Entrada de dados

#(Variaveis)

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota 1:  "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

#(Processamento)

#Calculo da  média

media =(nota1 +nota2 + nota3) / 3

#Saida de dados

#(Regras para a aprovação e a reprovação)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovação")

#(Exibição dos resultados)

print(f"Nome do aluno: {nome}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média final: {media: .2f}")