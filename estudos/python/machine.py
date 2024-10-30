# condição
print("Bem-vindo ao jogo")

inventario = []

# Usar um loop while para simular um jogo
while True:

    print("\n1. Ir para cabana")
    print("2. Ir para o lago")
    print("3. Inventário")
    print("4. Sair")
    escolha = int(input("Qual sua escolha? "))

    if escolha == 1:
        explorando = True
        while explorando:
            print("\nVocê entrou em uma cabana. Você achou um item! Deseja pegar?")
            print("1. Sim")
            print("2. Não")
            print("3. Inventário")
            print("4. Sair da cabana")

            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                inventario.append("espada")
                print("Você achou uma espada!")
                print("\nDeseja continuar explorando?")
                print("1. Sim")
                print("2. Sair da cabana")
                opcao2 = int(input("Escolha uma opção: "))
                
                if opcao2 == 1:
                    print("Você não achou nada dessa vez.")
                elif opcao2 == 2:
                    explorando = False  
            elif opcao == 2:
                print("Você deixou o item de lado.")
            elif opcao == 3:
                print("Inventário:")
                if inventario:
                    for item in inventario:
                        print(f"- {item}")
                else:
                    print("Inventário vazio.")
            elif opcao == 4:
                explorando = False  
            else:
                print("Opção inválida.")

    elif escolha == 2:
        print("Você foi para o lago.")
    elif escolha == 3:
        print("Inventário:")
        if inventario:
            for item in inventario:
                print(f"- {item}")
        else:
            print("Inventário vazio.")
    elif escolha == 4:
        print("Você saiu do jogo.")
        break
    else:
        print("Escolha inválida.")