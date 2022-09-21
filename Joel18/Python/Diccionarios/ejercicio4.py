# Ejericio 4: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuya llave sea un número.

dictionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "1": 6, "2": 7}
dictionario2 = {}

for key, value in dictionario.items():
    if not key.isnumeric():
        dictionario2[key] = value

print(dictionario2)