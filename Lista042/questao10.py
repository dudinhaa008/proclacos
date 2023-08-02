"""
10. Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
Média Situação
Abaixo de 3,0 Reprovado
Entre 3,0 e 6,9 Prova Final
A partir de 7,0 Aprovado
"""
nome_aluno = input("Digite o nome do aluno: ")
nota_prova1 = float(input("Digite a nota da prova 1: "))
nota_prova2 = float(input("Digite a nota da prova 2: "))

media = (nota_prova1 + nota_prova2) / 2

if media >= 7.0:
    situacao = "Aprovado"
if media >= 3.0:
    situacao = "Prova Final"
else:
    situacao = "Reprovado"

print(f"Nome do aluno: {nome_aluno}")
print(f"Média: {media:.2f}")
print(f"Situação: {situacao}")
