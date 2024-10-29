senha = 1234
tentativa = ''

print("Olá! Pode digitar sua senha?")

while tentativa != senha:
    tentativa = int(input("Digite sua senha: "))
    if tentativa != senha:
        print("oh no, its wrong, dude :<")

print("senha correta! :3")