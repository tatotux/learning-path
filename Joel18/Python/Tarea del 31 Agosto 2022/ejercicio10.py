# Ejercicio 10:
# Escribir un programa que muestre en pantalla la suma de todos los números de 2 listas.
# Ejemplo: 
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [6, 7, 8, 9, 10]
# suma = 55 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)

lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]

acumulado1 = 0
acumulado2 = 0

suma = 0

for a in lista1:
    acumulado1 = acumulado1 + a

for a in lista2:
    acumulado2 = acumulado2 + a


suma = acumulado1 + acumulado2

print(suma)