from pathlib import Path

# Definindo o caminho dos arquivos
caminho_do_cliente = Path("clientes_biblioteca.txt")
caminho_livro = Path("livros_clientes.txt")

# Cadastro do cliente
nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")

# Gerando número de cartão
try:
    with caminho_do_cliente.open() as arquivo:
        linhas = arquivo.readlines()
        numero_cartao = len(linhas) + 1  # Conta o número de linhas para gerar um novo número de cartão
except FileNotFoundError:
    numero_cartao = 1  # Se o arquivo não existir, define o primeiro número de cartão como 1

# Salvando os dados do cliente
with caminho_do_cliente.open(mode='a') as arquivo:
    arquivo.write(f"{numero_cartao}, {nome}, {telefone}\n")

print(f"Cliente cadastrado com sucesso! Seu número de cartão é: {numero_cartao}")

# Registro dos livros
numero_cartao = int(input("Digite seu número de cartão: "))
livros = input("Digite os livros que você quer pegar (separados por vírgulas): ")

while True:
    deseja_adicionar = input("Gostaria de ter mais livro? (sim/não): ")
    if deseja_adicionar == "sim":
        new_livros = input("Digite os livros que você quer adicionar (separados por vírgulas): ")
        livros += f", {new_livros}" # Adiciona os novos livros
    elif deseja_adicionar == "não":
        break
    else:
        print("Resposta inválida")

# Salvando os dados dos livros para o cliente
with caminho_livro.open(mode='a') as arquivo:
    arquivo.write(f"{numero_cartao}, {livros}\n")

print("Livros adicionados com sucesso!")

# Consulta de livros por número de cartão
numero_cartao = int(input("Digite seu número de cartão para consultar os livros: "))

try:
    with caminho_livro.open() as arquivo:
        linhas = arquivo.readlines()
        encontrou = False
        for linha in linhas:
            num_cartao, livros = linha.strip().split(', ', 1)
            if int(num_cartao) == numero_cartao:
                print(f"Livros pegados: {livros}")
                encontrou = True
                break
        if not encontrou:
            print("Nenhum livro encontrado para este número de cartão.")
except FileNotFoundError:
    print("Nenhum registro foi encontrado.")