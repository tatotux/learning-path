# Ejercicio 1: Escribir un programa que lea todos los elementos de un diccionario y los muestre en pantalla.

dictionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for key, value in dictionario.items():
    print(key, value)