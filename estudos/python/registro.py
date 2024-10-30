from pathlib import Path

registro = Path("banco.txt")

dados = input("Registre os nomes (separe-os por vírgula): ").split(',')

with registro.open(mode='w') as arquivo:
    for item in dados:
        arquivo.write(f"{item.strip()}\n")  

print("Nomes adicionados com sucesso!")

with registro.open(mode='r') as arquivo:
    dados = arquivo.readlines()

dados = [linha.strip() for linha in dados]

print("Dados recebidos:", dados)