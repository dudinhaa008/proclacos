valor4 = 0.7536
# Formatação float exibindo em percentual com decimal em 1 dígito
print(f"Valor 4: {valor4:.1%}")

# Incluindo R$ antes do valor e substituindo a vírgula do milhar por underline
texto_valor2 = f"R$ {valor2:_.2f}"
print(f"Texto Valor 2: {texto_valor2}")

# Substituindo o que é ponto por vírgula e o que é underline por ponto
texto_valor_br = texto_valor2.replace(".",",").replace("_",".")
print(f"Texto Valor BR: {texto_valor_br}")
