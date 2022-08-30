arreglo_uno = {'MexicoDF': 123456, 'San Jose': 22000, 'Austin': 120202, 'Texas': 32221}

arreglo_dos = []

for numero in arreglo_uno.values():
    arreglo_dos.append(numero)

tamano = len(arreglo_dos)

for i in range(tamano):
    for j in range(0, tamano-i-1):
        if arreglo_dos[j] > arreglo_dos[j+1]:
            arreglo_dos[j], arreglo_dos[j+1] = arreglo_dos[j+1], arreglo_dos[j]

print(arreglo_dos)