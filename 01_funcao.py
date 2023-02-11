def imc(peso, altura):
    return peso / altura ** 2

resultado = imc(81, 1.72)

print("o IMC calculado é", resultado)

############################################################

from math import pi

def calcular_area(base, altura, tipo):
    if tipo == "R": 
        return base * altura
    elif tipo == "T":
        return base * altura / 2
    elif tipo == "E":
        return (base / 2) * (altura / 2) * pi
    else None