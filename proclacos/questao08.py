"""
8) Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar,
mostre-o; não sendo, passe para o próximo passo.

"""
numero = 0

while numero <= 20:
    if numero % 2 != 0:
        print(numero)
    numero += 1