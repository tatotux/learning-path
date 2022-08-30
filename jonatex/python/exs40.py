arreglo_uno = [5,3,4,1,7]
arreglo_dos = []

for numero_arreglo_uno in arreglo_uno:
    if not arreglo_dos:
        arreglo_dos.append(numero_arreglo_uno)
    else:
        if numero_arreglo_uno not in arreglo_dos:
            if numero_arreglo_uno > arreglo_dos[-1]:
                arreglo_dos.append(numero_arreglo_uno)
            else:
                index = 0 
                for numero_arreglo_dos in arreglo_dos:
                    if numero_arreglo_dos > numero_arreglo_uno:
                     arreglo_dos.insert(index, numero_arreglo_dos)
                     index = index + 1
                    
                        

print(arreglo_dos)arreglo_uno = [5, 4, 3, 2, 5, 1]
tamano = len(arreglo_uno)

for i in range(tamano):
    for j in range(0, tamano-i-1):
        if arreglo_uno[j] > arreglo_uno[j+1]:
            arreglo_uno[j], arreglo_uno[j+1] = arreglo_uno[j+1], arreglo_uno[j]

print(arreglo_uno)