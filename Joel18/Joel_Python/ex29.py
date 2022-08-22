i=21  #33 #35
numbers = []  #Numbers now:  [21, 23, 25, 27, 29, 31, 33]
while i < 35: 
    print(f"At the top i is {i}")
    numbers.append(i)
    i=i+2  #va a ser 35
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")  #i es 35 pero no se a agregado
print("The numbers: ")
for num in numbers:
    print(num)