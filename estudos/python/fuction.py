import math

def pitagroas(cateto_a, cateto_b):
    #Calcula a hipotenusa com base nos catetos
    hipotenusa = math.sqrt(cateto_a ** 2 + cateto_b ** 2)
    return hipotenusa

#Exemplo de uso
cateto_a = float(input("Digite o valor de A: "))
cateto_b = float(input("Digite o valor de B: "))
hipotenusa = pitagroas(cateto_a, cateto_b)
print(f"O valor da hispitenusa é: {hipotenusa}")