import random

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def my_shuffle(arr):
    for i in range(0, len(arr)):
        swap(arr, random.randint(0, len(arr) - 1), random.randint(0, len(arr) - 1))
    return arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
print(my_shuffle(arr))