nome1 = str(input("Digite o primeiro nome: "))
nome2 = str(input("Digite o primeiro nome: "))

idade1 = int(input(f"Digite a idade do {nome1}: "))
idade2 = int(input(f"Digite a idade do {nome2}: "))

# print("o",nome1,"tem",idade1)
# print("o"+nome2+"tem"+str(idade2))
# print(f"O {nome1} tem {idade2}")

if(idade1>idade2):
    print(f"o {nome1} é mais velho que o {nome2}")
if(idade1==idade2):
    print(f"as idades do {nome1} e {nome2} sao iguais")
else:
    print(f"o {nome2} é mais velho que o {nome1}")
