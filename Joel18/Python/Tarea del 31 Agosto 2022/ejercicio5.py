# Ejercicio 5:
# Escribir un programa que un número entero y muestre en pantalla si es divisible entre 3 o 5.

numero = [5,3]

for a in numero:
    if a %5 == 0 or a %3 == 0:
         print("Es divisible entre 5 y 3")
    else:
        print("No es divisible entre 5 y 3")
    
