#Muestre la forma de obtener uno de cada tres elementos de la lista, por ejemplo:

#arr = [1,2,3,4,8,3,43,42,434,34,54,52,565,657] y tiene que mostrar los siguientes:

#1
#4
#43
#34
#565

lista = [1,2,3,4,8,3,43,42,434,34,54,52,565,657]

for a in range(0, len(lista), 3):
    print(lista[a])


