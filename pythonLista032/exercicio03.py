"""
3) Desenvolver um programa que pergunte ao usuário o seu peso (em quilos) e sua altura (em metros). Ao final o
programa deverá exibir na tela para o usuário o valor do peso informado em gramas e a altura em centímetros.
"""
peso = float(input("Informe seu peso em quilos"))
altura = float(input("Informe sua altura em metros"))

IMC = peso / altura

print("seu imc é", IMC)
