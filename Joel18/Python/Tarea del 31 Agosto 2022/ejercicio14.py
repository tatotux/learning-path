# Ejercicio 14:
# Escribir un programa que muestre en pantalla promedio de los elementos de una lista.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 15/5 = 3



lista = [1, 2, 3, 4, 5, 6, 7 ,8, 9 ,10, 11, 12]

suma = 0 

for a in lista:
    suma = suma + a

promedio = int(suma/len(lista))

print(promedio)
