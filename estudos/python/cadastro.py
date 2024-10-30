frutas = []

while True: 
    fruta = input("digite um nome de uma fruta ou saia: ")
    if fruta.lower() == 'sair' :
        break

    frutas.append(fruta)

print("lista de frutas : ")
for fruta in frutas:
    print(fruta)