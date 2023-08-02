"""
1. Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000.
"""
def main():
    numero = int(input("Digite um número: "))

    if numero > 1000:
        print("O número digitado está acima de 1000.")
    elif numero < 1000: