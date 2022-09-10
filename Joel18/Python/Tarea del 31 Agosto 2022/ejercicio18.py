# Ejercicio 18:
# Escribir un programa que muestre en pantalla el número mayor entre 2 listas.
# Ejemplo: lista1 = [1, 2, 3, 4, 5] lista2 = [6, 7, 8, 9, 10] el número mayor es 10

lista1 = [1, 2, 3, 400, 5]
lista2 = [6, 7, 8, 900, 10]

union = lista1 + lista2

mayor = union[0]

for a in range(0,len(union)):
    if union[a] > mayor:
        mayor = union[a]

print(mayor)