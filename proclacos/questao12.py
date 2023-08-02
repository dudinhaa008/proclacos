"""
12) Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média.
"""

maior = float('-inf')
menor = float('inf')
soma = 0
contador = 0

while True:
    numero = float(input("Digite um número real (ou -1 para sair): "))

    if numero == -1:
        break

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    soma += numero
    contador += 1

if contador == 0:
    print("Nenhum número foi inserido.")
else:
    media = soma / contador
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")
    print(f"A média dos números é: {media}")