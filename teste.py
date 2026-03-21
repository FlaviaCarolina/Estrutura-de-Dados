nome1 = str(input("Digite o primeiro nome: "))
nome2 = str(input("Digite o primeiro nome: "))

idade1 = int(input(f"Digite a idade do {nome1}: "))
idade2 = int(input(f"Digite a idade do {nome2}: "))

# print("o",nome1,"tem",idade1)
# print("o"+nome2+"tem"+str(idade2))
# print(f"O {nome1} tem {idade2}")

if(idade1>idade2):
    diferencaDeIdade = idade1-idade2
    print(f"o {nome1} é mais velho que o {nome2}, com diferenca de {diferencaDeIdade} anos")
elif(idade1==idade2):
    print(f"as idades do {nome1} e {nome2} sao iguais")
else:
    diferencaDeIdade = idade2-idade1
    print(f"o {nome2} é mais velho que o {nome1}, com diferenca de {diferencaDeIdade} anos")

mesNascimento = int(input("ensira seu mes de nascimento no formato: 0"))
if(mesNascimento == 1):
    print("seu mes de aniversario é janeiro")
elif (mesNascimento == 2):
    print("seu mes de aniversario é fevereiro")
elif (mesNascimento == 3):
    print("seu mes de aniversario é março")
elif (mesNascimento == 4):
    print("seu mes de aniversario é abril")
elif (mesNascimento == 5):
    print("seu mes de aniversario é maio")
elif (mesNascimento == 6):
    print("seu mes de aniversario é junho")
elif (mesNascimento == 7):
    print("seu mes de aniversario é julho")
elif (mesNascimento == 8):
    print("seu mes de aniversario é agosto")
elif (mesNascimento == 9):
    print("seu mes de aniversario é setembro")
elif (mesNascimento == 10):
    print("seu mes de aniversario é outubro")
elif (mesNascimento == 11):
    print("seu mes de aniversario é novembro")
elif (mesNascimento == 12):
    print("seu mes de aniversario é dezembro")
else:
    print("mes invalido")


