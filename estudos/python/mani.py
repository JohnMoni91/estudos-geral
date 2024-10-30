from pathlib import Path

#Define o caminho do arquivo
caminho_do_arquivo = Path("meus_dados.txt")

#Dados para salvar no arquivo
dados_para_salvar = ["python", "C++", "Java"]

#Abre o caminho no modo 'w' (escrita) e salva os dados
with caminho_do_arquivo.open(mode='w') as arquivo:
    for item in dados_para_salvar:
        arquivo.write(f"{item}\n")

print("Dados salvos")

#Abre o arquivo no modo 'r' (leitura) e lê os dados
with caminho_do_arquivo.open(mode='r') as arquivo:
    dados_lidos = arquivo.readlines()

#Remove os caracteres de nova linha
dados_lidos = [linha.strip() for linha in dados_lidos]

print("Dados lidos do arquivo: ", dados_lidos)