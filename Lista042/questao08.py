"""
8. Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final
"""
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


maior = num1

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print("O maior número é:", maior)