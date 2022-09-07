# Ejercicio 1:
# Escribir un programa que un número entero y muestre en pantalla si es par o impar.
# Así espero su respuesta en todos los ejercicios siguientes.
numero = 46
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

# Ejercicio 2:
# Escribir un programa que un número entero y muestre en pantalla si es positivo, negativo o cero.
numero = 10 
if numero == 0 :
    print("es igual a cero")
elif numero < 0:
    print("es negativo")
else :
    print("es positivo")
# Ejercicio 3:
# Escribir un programa que un número entero y muestre en pantalla si es divisible entre 5.
numero = 25
if numero // 5 :
    print("el numero si es divisible entre 5")
else:
    print("no es divisible entre 5")
# Ejercicio 4:
# Escribir un programa que un número entero y muestre en pantalla si es divisible entre 3 y 5.
numero = 9
if numero % 5:
    print("el numero es divisible por 5")
elif numero % 3:
        print("el numero es divisible por 3")
else:
    ("no es divisible por 3 ni por 5")
# Ejercicio 5:
# Escribir un programa que un número entero y muestre en pantalla si es divisible entre 3 o 5.
numero = 35
if numero % 5:
    print("el numero es divisible por 5")
elif numero % 3:
        print("el numero es divisible por 3")
else:
    ("no es divisible por 3 ni por 5")
# Ejercicio 6:
# Escribir un programa que muestre en pantalla la cantidad de elementos en una lista.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 5
lista = [1,2,3,4,5]
print("la cantidad de elementos de la lista son :" , len (lista))
# Ejercicio 7:
# Escribir un programa que muestre en pantalla la suma de todos los elementos de una lista.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 15
lista = [1, 2, 3, 4, 5]
lista2 = 0
lista3 = 0
for numero in lista :
    lista2 = lista2 + numero
    print("la suma de la lista del ejercicio 7 es : " , lista2)
# Ejercicio 8:
# Escribir un programa que muestre en pantalla la suma de todos los elementos de una lista que sean pares.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 6
lista = [1, 2, 3, 4, 5]
pares = 0
for numero in lista:
    if numero % 2 == 0:
       pares += numero
       print("la suma de los numeros pares de el ejercicio 8 es : " , pares)
# Ejercicio 9:
# Escribir un programa que muestre en pantalla la suma de todos los elementos de una lista que sean impares.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 9
lista = [1, 2, 3, 4, 5]
impares = 0
for numero in lista:
    if numero % 2 == 1:
       impares += numero
       print("la suma de los numeros pares de el ejercicio 9 es : " , impares)
# Ejercicio 10:
# Escribir un programa que muestre en pantalla la suma de todos los números de 2 listas.
# Ejemplo: 
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [6, 7, 8, 9, 10]
# suma = 55 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
resultado1 = 0
resultado2 = 0
for x in lista1:
    resultado1 += x
for y in lista2:
    resultado2 += y
print("la suma de las listas de ejercicio 10 es :" , resultado1 + resultado2 )
# Ejercicio 11:
# Escribir un programa que muestre en pantalla solo los index de los elementos de una lista que sean pares.
# Ejemplo: lista = [1, 2, 3, 4, 5] = [3, 5] (Por que los pares son el index 2 es par y el index 4 es par)
lista = [1, 2, 3, 4, 5]
print("los index pares en la lista del ejercicio 11 son : " , (lista.index(2)) , (lista.index(4)))
# Ejercicio 12:
# Escribir un programa que muestre en pantalla el último elemento de una lista.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 5
lista = [1, 2, 3, 4, 5]

print("el ultimo elemento de la lista del ejercicio 9 es :" , (lista[-1]) )
# Ejercicio 13:
# Escribir un programa que muestre en pantalla el primer elemento de una lista.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 1
lista = [1, 2, 3, 4, 5]
print("el primer elemento de la lista de el ejercicio 13 es :" , (lista[0]))
# Ejercicio 14:
# Escribir un programa que muestre en pantalla promedio de los elementos de una lista.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 15/5 = 3
lista = [1, 2, 3, 4, 5]
promedio = 0 
y = 0
for x in lista:
    y += x
    promedio = y/5 
    print("el promedio de los elementos de la lista del ejercicio 14 son : " , promedio)
# Ejercicio 15:
# Escribir un programa que muestre en pantalla el número menor de una lista.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 1
lista = [1, 2, 3, 4, 5]
for x in lista:
    if x <= 1:
        print("el numero menor de la lista del ejercicio 15 es : " , x)
# Ejercicio 16:
# Escribir un programa que muestre en pantalla el número mayor de una lista.
# Ejemplo: lista = [1, 2, 3, 4, 5] = 5
lista = [1, 2, 3, 4, 5] 
for x in lista:
    if x >= 5:
        print("el numero mayor de el ejercicio 16 es :" , x)

# Ejercicio 17:
# Escribir un programa que muestre en pantalla la unión de dos listas.
# Ejemplo: lista1 = [1, 2, 3, 4, 5] lista2 = [6, 7, 8, 9, 10] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = 0 
lista3 = lista1 + lista2
print("la union de las dos listas en el ejercicio 17 es : " ,lista3)
# Ejercicio 18:
# Escribir un programa que muestre en pantalla el número mayor entre 2 listas.
# Ejemplo: lista1 = [1, 2, 3, 4, 5] lista2 = [6, 7, 8, 9, 10] el número mayor es 10
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = 0 
lista3 = lista1 + lista2
for x in lista3:
    if x >= 10:
        print("el numero mayor entre 2 listas del ejercicio 18 es :" , x)
