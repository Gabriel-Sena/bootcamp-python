nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
idade = input("Informe sua idade: ")

#end e separador padrão
print(nome, idade)

#trocando apenas o end
print(nome, idade, end="...\n")

#trocando apenas o separador
print(nome, idade, sep="-")

#trocando os dois
print(nome, sobrenome, idade, sep="-", end=" é lindão")