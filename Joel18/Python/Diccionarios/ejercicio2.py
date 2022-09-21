# Ejericio 2: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuya llave comience con la letra "a".
dictionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
dictionario2 = {}

for key, value in dictionario.items():
    if key != "a":
        dictionario2[key] = value

print(dictionario2)