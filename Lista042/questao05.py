"""
5. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
"""
sigla_estado = input("Digite a sigla de um estado brasileiro: ")

sigla_estado = sigla_estado.upper()

if sigla_estado in ["SP", "RJ", "MG", "ES"]:
    print("O estado inserido está na região Sudeste.")
else:
    print("O estado inserido não está na região Sudeste.")