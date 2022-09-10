# Ejercicio 4:
# Escribir un programa que un número entero y muestre en pantalla si es divisible entre 3 y 5.


numero = [5,15]

for a in numero:
    if a %5 == 0 and a %3 == 0:
         print("Es divisible entre 5 y 3")
    else:
        print("No es divisible entre 5 y 3")
    