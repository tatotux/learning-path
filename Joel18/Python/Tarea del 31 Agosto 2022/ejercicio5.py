# Ejercicio 5:
# Escribir un programa que un número entero y muestre en pantalla si es divisible entre 3 o 5.

numero = [5,3]

for a in numero:
    if a %5 == 0:
         print("Es divisible entre 5")
    else:
        print("No es divisible entre 5")
    
    if a %3 == 0:
         print("Es divisible entre 3")
    else:
        print("No es divisible entre 3")
    
