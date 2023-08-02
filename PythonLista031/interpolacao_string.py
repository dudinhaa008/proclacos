nome = input("Digite o seu primeiro nome: ")
idade = int(input("Digite sua idade: "))

#print("olá, ", nome, "!")
#print("Tudo bem com você?")
#print("Caramba", nome, "! você tem", idade, "anos? Nem parece.")

print("olá, {}!".format(nome))
print("Tudo bem com você?")


print("Caramba", nome, "! você tem", idade, "anos? Nem parece.")
print("Caramba {}! você tem {} anos? Nem parece.".format(nome, idade))
print(f"caramba {nome}! você tem {idade} anos? nem parece.")
