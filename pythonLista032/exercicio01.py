"""
1) Desenvolver um programa que pergunte o valor da conta a ser paga no restaurante e exiba como resposta o
valor com o acréscimo dos 10% da gorjeta do garçom.
"""
conta = float(input("informe o valor da conta "))

acrescimo = conta * 10 / 100

total = conta + acrescimo

print(total)
