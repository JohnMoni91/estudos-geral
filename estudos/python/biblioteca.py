from pathlib import Path

caminho_do_arquivo = Path("clientes_biblioteca.txt")

nome = input("Digite seu nome: ")
telefone = input("Digite seu telefone: ")
numero_do_cartao = input("Digite o seu número do cartão: ")

with caminho_do_arquivo.open(mode = 'a') as arquivo:
    arquivo.write("{nome}, {telefone}, {numero_do_cartao}\n")

    print("cliente cadastrado com sucesso!")