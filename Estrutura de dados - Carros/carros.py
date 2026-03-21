# Guarda o nome do arquivo CSV em uma variável.
ARQUIVO_CSV = "base_dados_carros.csv"


# Cria uma função para carregar os dados do arquivo.
def carregar_dados():
    # Cria uma lista vazia para guardar todos os carros.
    carros = []

    # Abre o arquivo CSV para leitura.
    arquivo = open(ARQUIVO_CSV, "r")
    # Lê somente a primeira linha do arquivo.
    primeira_linha = arquivo.readline()
    # Remove a quebra de linha e separa o cabeçalho pelo ponto e vírgula.
    cabecalho = primeira_linha.strip().split(";")

    # Lê o restante do arquivo linha por linha.
    for linha in arquivo:
        # Remove a quebra de linha e separa os dados pelo ponto e vírgula.
        dados = linha.strip().split(";")
        # Cria um dicionário vazio para montar um carro.
        carro = {}

        # Repete para cada posição do cabeçalho.
        for i in range(len(cabecalho)):
            # Pega o nome da coluna.
            chave = cabecalho[i]
            # Pega o valor da coluna na linha atual.
            valor = dados[i]
            # Guarda a informação no dicionário do carro.
            carro[chave] = valor

        # Converte o preço de texto para número decimal.
        carro["PRECO"] = float(carro["PRECO"])
        # Adiciona o carro na lista de carros.
        carros.append(carro)

    # Fecha o arquivo depois da leitura.
    arquivo.close()

    # Devolve a lista com todos os carros.
    return carros


# Cria uma função para transformar um carro em texto.
def formatar_carro(carro):
    # Retorna um bloco de texto com os dados do carro.
    return (
        # Mostra o ID do carro.
        f"ID: {carro['ID']}\n"
        # Mostra a marca do carro.
        f"Marca: {carro['MARCA']}\n"
        # Mostra o modelo do carro.
        f"Modelo: {carro['MODELO']}\n"
        # Mostra o preço do carro.
        f"Preco: R$ {carro['PRECO']:.2f}\n"
        # Mostra o país do carro.
        f"Pais: {carro['PAIS']}\n"
        # Mostra a região do carro.
        f"Regiao: {carro['REGIAO']}\n"
        # Mostra o nome ligado ao carro.
        f"Nome: {carro['NOME']}\n"
        # Mostra a data do carro.
        f"Data: {carro['DATA']}\n"
    )


# Cria uma função para salvar qualquer relatório em arquivo texto.
def salvar_relatorio(nome_arquivo, titulo, carros):
    # Guarda o nome do arquivo em uma variável.
    caminho = nome_arquivo

    # Abre o arquivo para escrita.
    with open(caminho, "w", encoding="utf-8") as arquivo:
        # Escreve o título do relatório.
        arquivo.write(titulo + "\n")
        # Escreve uma linha de separação.
        arquivo.write("=" * len(titulo) + "\n\n")
        # Escreve a quantidade de carros do relatório.
        arquivo.write(f"Total de carros: {len(carros)}\n\n")

        # Percorre todos os carros da lista.
        for carro in carros:
            # Escreve os dados formatados do carro.
            arquivo.write(formatar_carro(carro))
            # Escreve uma linha para separar um carro do outro.
            arquivo.write("-" * 40 + "\n")

    # Devolve o nome do arquivo salvo.
    return caminho


# Cria a função do relatório 1.
def relatorio_1(carros):
    # Ordena os carros pela marca em ordem alfabética.
    carros_ordenados = sorted(carros, key=lambda carro: carro["MARCA"].lower())
    # Salva e devolve o relatório pronto.
    return salvar_relatorio(
        # Define o nome do arquivo do relatório 1.
        "relatorio_1_todos_por_marca.txt",
        # Define o título do relatório 1.
        "RELATORIO 1 - TODOS OS CARROS EM ORDEM DE MARCA",
        # Envia a lista ordenada para salvar.
        carros_ordenados,
    )


# Cria a função do relatório 2.
def relatorio_2(carros):
    # Pede ao usuário o país desejado.
    pais = input("Digite o pais desejado: ").strip()

    # Cria uma lista vazia para os carros filtrados.
    carros_filtrados = []
    # Percorre todos os carros.
    for carro in carros:
        # Verifica se o país do carro é igual ao digitado.
        if carro["PAIS"].lower() == pais.lower():
            # Adiciona o carro na lista filtrada.
            carros_filtrados.append(carro)

    # Ordena os carros filtrados pela marca.
    carros_ordenados = sorted(carros_filtrados, key=lambda carro: carro["MARCA"].lower())

    # Salva e devolve o relatório pronto.
    return salvar_relatorio(
        # Define o nome do arquivo do relatório 2.
        "relatorio_2_por_pais.txt",
        # Define o título do relatório 2.
        f"RELATORIO 2 - CARROS DO PAIS {pais.upper()}",
        # Envia a lista ordenada para salvar.
        carros_ordenados,
    )


# Cria a função do relatório 3.
def relatorio_3(carros):
    # Pede ao usuário o modelo desejado.
    modelo = input("Digite o modelo desejado: ").strip()

    # Cria uma lista vazia para os carros filtrados.
    carros_filtrados = []
    # Percorre todos os carros.
    for carro in carros:
        # Verifica se o modelo do carro é igual ao digitado.
        if carro["MODELO"].lower() == modelo.lower():
            # Adiciona o carro na lista filtrada.
            carros_filtrados.append(carro)

    # Ordena os carros filtrados pelo país.
    carros_ordenados = sorted(carros_filtrados, key=lambda carro: carro["PAIS"].lower())

    # Salva e devolve o relatório pronto.
    return salvar_relatorio(
        # Define o nome do arquivo do relatório 3.
        "relatorio_3_por_modelo.txt",
        # Define o título do relatório 3.
        f"RELATORIO 3 - CARROS DO MODELO {modelo.upper()}",
        # Envia a lista ordenada para salvar.
        carros_ordenados,
    )


# Cria a função do relatório 4.
def relatorio_4(carros):
    # Procura o menor preço da lista.
    menor_preco = min(carro["PRECO"] for carro in carros)
    # Procura o maior preço da lista.
    maior_preco = max(carro["PRECO"] for carro in carros)

    # Cria uma lista vazia para os carros mais baratos.
    carros_mais_baratos = []
    # Cria uma lista vazia para os carros mais caros.
    carros_mais_caros = []

    # Percorre todos os carros.
    for carro in carros:
        # Verifica se o carro tem o menor preço.
        if carro["PRECO"] == menor_preco:
            # Adiciona o carro na lista dos mais baratos.
            carros_mais_baratos.append(carro)

        # Verifica se o carro tem o maior preço.
        if carro["PRECO"] == maior_preco:
            # Adiciona o carro na lista dos mais caros.
            carros_mais_caros.append(carro)

    # Define o nome do arquivo do relatório 4.
    caminho = "relatorio_4_maior_e_menor_preco.txt"

    # Abre o arquivo do relatório 4 para escrita.
    with open(caminho, "w", encoding="utf-8") as arquivo:
        # Guarda o título do relatório 4.
        titulo = "RELATORIO 4 - CARROS MAIS BARATOS E MAIS CAROS"
        # Escreve o título no arquivo.
        arquivo.write(titulo + "\n")
        # Escreve uma linha de separação.
        arquivo.write("=" * len(titulo) + "\n\n")

        # Escreve o menor preço encontrado.
        arquivo.write(f"Menor preco encontrado: R$ {menor_preco:.2f}\n\n")
        # Percorre os carros mais baratos.
        for carro in carros_mais_baratos:
            # Escreve os dados do carro mais barato.
            arquivo.write(formatar_carro(carro))
            # Escreve uma linha de separação.
            arquivo.write("-" * 40 + "\n")

        # Escreve o maior preço encontrado.
        arquivo.write(f"\nMaior preco encontrado: R$ {maior_preco:.2f}\n\n")
        # Percorre os carros mais caros.
        for carro in carros_mais_caros:
            # Escreve os dados do carro mais caro.
            arquivo.write(formatar_carro(carro))
            # Escreve uma linha de separação.
            arquivo.write("-" * 40 + "\n")

    # Devolve o nome do arquivo salvo.
    return caminho


# Cria uma função para mostrar o menu na tela.
def mostrar_menu():
    # Mostra o título do menu.
    print("\nMENU DE RELATORIOS")
    # Mostra a opção 1.
    print("1 - Relatorio com todos os carros por marca")
    # Mostra a opção 2.
    print("2 - Relatorio com carros de um pais")
    # Mostra a opção 3.
    print("3 - Relatorio com carros de um modelo")
    # Mostra a opção 4.
    print("4 - Relatorio com carros mais baratos e mais caros")
    # Mostra a opção para sair.
    print("0 - Sair")


# Cria a função principal do programa.
def main():
    # Carrega todos os dados dos carros.
    carros = carregar_dados()

    # Cria um laço para repetir o menu até o usuário sair.
    while True:
        # Mostra o menu na tela.
        mostrar_menu()
        # Pede a opção escolhida pelo usuário.
        opcao = input("Escolha uma opcao: ").strip()

        # Verifica se o usuário escolheu a opção 1.
        if opcao == "1":
            # Gera o relatório 1.
            caminho = relatorio_1(carros)
            # Mostra onde o relatório foi salvo.
            print(f"Relatorio salvo em: {caminho}")
        # Verifica se o usuário escolheu a opção 2.
        elif opcao == "2":
            # Gera o relatório 2.
            caminho = relatorio_2(carros)
            # Mostra onde o relatório foi salvo.
            print(f"Relatorio salvo em: {caminho}")
        # Verifica se o usuário escolheu a opção 3.
        elif opcao == "3":
            # Gera o relatório 3.
            caminho = relatorio_3(carros)
            # Mostra onde o relatório foi salvo.
            print(f"Relatorio salvo em: {caminho}")
        # Verifica se o usuário escolheu a opção 4.
        elif opcao == "4":
            # Gera o relatório 4.
            caminho = relatorio_4(carros)
            # Mostra onde o relatório foi salvo.
            print(f"Relatorio salvo em: {caminho}")
        # Verifica se o usuário escolheu sair.
        elif opcao == "0":
            # Mostra a mensagem de encerramento.
            print("Programa encerrado.")
            # Interrompe o laço.
            break
        # Se a opção for diferente das válidas.
        else:
            # Mostra uma mensagem de erro.
            print("Opcao invalida. Tente novamente.")


# Verifica se este arquivo está sendo executado diretamente.
if __name__ == "__main__":
    # Chama a função principal.
    main()
