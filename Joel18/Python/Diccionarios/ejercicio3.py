# Ejericio 3: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuyo valor sea menor a 5.

dictionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
dictionario2 = {}

for key, value in dictionario.items():
    if value >= 5:
        dictionario2[key] = value

print(dictionario2)