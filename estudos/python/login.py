#projeto lojinha

def cadastro_cliente(nome, email, telefone):
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{nome}, {email}, {telefone}\n")
        print("Cliente cadastrado!")

def lista_cliente():
    try:
        with open("clientes.txt", "r") as arquivo:
            clientes = arquivo.readlines()
            if not clientes:
                 print("Nenhum cliente encontrado")
            else:
                print("Lista de clientes já cadastrado: ")
                for cliente in clientes:
                    nome, email, telefone = cliente.strip().split(",")
                    print(f"Nome: {nome}, email: {email}, telefone: {telefone}")
    except: FileNotFoundError
    print("Nenhum cliente encontrado.")

    #manipulação do arquivo

def salvar_em_arquivo(dados, nomes_arquivo):
    with open (nomes_arquivo, "r") as arquivo:
        for dado in dados: 
            arquivo.write(f"{dado}\n")

def ler_de_arquivo(nome_arquivo):
    try:
        with open (nome_arquivo, "r") as arquivo:
            return arquivo.readlines
    except FileNotFoundError:
        return[]


def login():
    while True:
        print("\n--- Menu ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("digita o nome: ")
            email = input("Digite o email: ")
            telefone = input("Digite o telefone: ")
            cadastro_cliente(nome, email, telefone)
        elif opcao == "2":
            lista_cliente()
        elif opcao == "3":
            print ("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

#Execute o programa
login()