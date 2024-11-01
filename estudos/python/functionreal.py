def verifyId(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "M5enor de idade"
    
idade_usuario = int(input("Sua idade: "))

status = verifyId(idade_usuario)

print(f"vc eh {status}")
