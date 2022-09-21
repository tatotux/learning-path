# Ejericio 5: Escribir un programa que lea un diccionario y cree una copia del mismo sin los elementos cuyo valor sea un número.

dictionario = {"a": 1, "b": 2, "c": 3, "d": "hola", "e": "mundo"}
dictionario2 = {}

for key, value in dictionario.items():
    if not (str(value).isnumeric()):
        dictionario2[key] = value

print(dictionario2)
