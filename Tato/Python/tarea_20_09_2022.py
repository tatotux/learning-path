# Ejercicios de la tarea 20/09/2022

# Ejercicio 1: Escribir un programa que lea todos los elementos de un diccionario y los muestre en pantalla.
# Respuesta 1:
dictionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for key, value in dictionario.items():
    print(key, value)

# Ejericio 2: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuya llave comience con la letra "a".
dictionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
dictionario2 = {}

for key, value in dictionario.items():
    if key != "a":
        dictionario2[key] = value


# Ejericio 3: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuyo valor sea menor a 5.

# Ejericio 4: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuya llave sea un número.

# Ejericio 5: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuyo valor sea un número.

# Ejericio 6: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuya llave sea un número par.

# Ejericio 7: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuyo valor sea un número par.

# Ejericio 8: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuya llave sea un número impar.

# Ejericio 9: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuyo valor sea un número impar.

# Ejericio 10: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuya llave sea un número primo.

dictionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
# Ejericio 11: Escribir un programa que lea un diccionario y traer el valor de la llave "b".

# Ejericio 12: Escribir un programa que lea un diccionario y traer 2 valores usando las llaves.

# Ejericio 13: Escribir un programa que lea un diccionario y traer solo las llaves.

# Ejericio 14: Escribir un programa que lea un diccionario y traer solo los valores.

