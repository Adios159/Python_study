import random

def my_choice(arr):
    return arr[random.randint(0, len(arr))]

arr = []
for i in range(0, 9):
    x = random.randint(0, 100)
    arr.append(x)

print(my_choice(arr))