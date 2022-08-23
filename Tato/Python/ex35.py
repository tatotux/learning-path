ten_things = "Manzanas Naranjas Coronas Telefono Luz Azucar"
print("Espere! no hay 10 cosas en la lista, Arreglemos eso")
stuff = ten_things.split(' ')
more_stuff = ["Dia", "Noche", "Cancion", "Frisbee",
              "Maiz", "Banano", "Mujer", "Hombre"]
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Agregando: ", next_one) 
    stuff.append(next_one)
    print(f"Aqui hay {len(stuff)} articulos ahora.")
    
print("Aqui vamos!: ", stuff)
print("Hagamos algo con estas cosas.")
print(stuff[1])
print(stuff[-1]) # wow que tuanis esa impresion! print(stuff.pop())
print(' '.join(stuff)) # que chiva! print('#'.join(stuff[3:5])) # super stellar!