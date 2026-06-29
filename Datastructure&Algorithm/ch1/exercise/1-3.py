import random

def minmax(arr):
    min = arr[0]
    max = arr[0]
    for i in arr[1:]:
        if(min > i):
            min = i
        if(max < i):
            max = i
    return (min, max)

arr = []
for i in range(0, 9):
    arr.append(random.randint(1, 100))

print(minmax(arr))