# condição
print("bem vindo ao jogo")
print("1. ir para cabana")
print("2. ir para o lago")
print("3. sair")

escolha = int(input("qual sua escolha? "))

if escolha == 1:
    print("vc entrou em casa. Vc achou um item! Deseja pegar?")
    print("1. sim")
    print("2. não")
    print("3. sair")

    opcao = int(input("deseja ver o q seria?"))
    if opcao == 1 :
        print("vc achou uma espada!")

        opcao2 = int(input("deseja continuar explorando?"))
        print ("1. sim")
        print ("2. não")
        if opcao2 == 1 :
            print("vc n achou nada")


    elif opcao == 2 :
        print("vc deixou de lado")
    elif opcao == 3 :
        print("vc saiu de casa")
    else:
        print("?")

elif escolha == 2:
    print("foi pro lago")

else:
    print("vc saiu do jogo")
