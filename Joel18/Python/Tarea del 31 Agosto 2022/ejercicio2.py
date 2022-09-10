# Escribir un programa que un número entero y muestre en pantalla si es positivo, negativo o cero.
numero = [12,-20,0]

for a in numero:
    if a > 0:
        print("positivo")
    else:
        if a < 0:
            print("negativo")
        else:
            a = 0
            print("cero")