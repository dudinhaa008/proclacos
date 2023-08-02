"""
6. Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
"""
ano_nascimento = int(input("Informe o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))


if ano_nascimento > ano_atual:
    print("Dados inseridos estão incorretos.")
else:
    idade = ano_atual - ano_nascimento
    print("A idade da pessoa é:", idade, "anos.")