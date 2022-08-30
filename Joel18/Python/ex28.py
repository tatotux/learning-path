la_cuenta = [9, 2, 6, 4, 8]
frutas = ['apples', 'oranges', 'pears', 'apricots']
cambio = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for numero in la_cuenta:
    print(f"Esta es la cuenta: {numero}")

for fruta in frutas:
    print(f"Es una fruta de tipo: {fruta}")

for i in cambio:
    print(f"Yo tengo: {i}")

elements = []
print(elements)

for i in range(10, 16):
    print(f"Adding {i} to the list.")
    elements.append(i)
print(elements)
print(elements[4])

for i in elements:
    print(f"Element was: {i}")  

