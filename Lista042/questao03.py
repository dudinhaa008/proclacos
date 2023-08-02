"""
3. Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, entre 5001 e 8000, ou acima de 8000.
"""
numero = float(input("Digite um número: "))


if numero < 1000:
    print("O número está abaixo de 1000.")
if 1000 <= numero <= 5000:
    print("O número está entre 1000 e 5000.")
if 5001 <= numero <= 8000:
    print("O número está entre 5001 e 8000.")
else:
    print("O número está acima de 8000.")