# Ejercicio 11:
# Escribir un programa que muestre en pantalla solo los index de los elementos de una lista que sean pares.
# Ejemplo: lista = [1, 2, 3, 4, 5] = [3, 5] (Por que los pares son el index 2 es par y el index 4 es par)


lista = [1, 2, 3, 4, 5, 6, 7]

for a in range(0, len(lista), 2):
    print(lista[a])
