"""
4. Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana.
"""
numero = int(input("Digite um número de 1 a 7: "))


if numero == 1:
    print("Domingo")
if numero == 2:
    print("Segunda-feira")
if numero == 3:
    print("Terça-feira")
if numero == 4:
    print("Quarta-feira")
if numero == 5:
    print("Quinta-feira")
if numero == 6:
    print("Sexta-feira")
if numero == 7:
    print("Sábado")
else:
    print("Número inválido")