acumulado1 = 0
acumulado2 = 0
final = 0 
arr1 = [1,2,3,4,5,6,7,8,9]
arr2 = [9,8,7,6,5,4,3,2,1]


if len(arr1) == len(arr2):
    for a in arr1:
        acumulado1 = acumulado1 + a

    for a in arr2:
       acumulado2 = acumulado2 + a
    final = acumulado1 + acumulado2
else:
    'esta mamando'  

    
print(final)