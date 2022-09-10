arr1 = [11,22,9,67,24]

arr2 = [34,55,88,99,30]

arr3 = []

x = 0
#arr3 = [45,77,97,166,54]

if len(arr1) == len(arr2):
    for a in arr1:
        arr3.append(arr1[x] + arr2[x])
        x = x + 1

print(arr3)
