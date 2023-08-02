"""
7. Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    maior = num1
    menor = num2
elif num2 > num1:
    maior = num2
    menor = num1
else:
    print("Os números são iguais:", num1)
    exit()
print("O maior número é:", maior)
print("O menor número é:", menor)