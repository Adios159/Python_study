def is_all_different(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if(arr[i] == arr[j]):
                return False
    return True

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 4, 2, 1]

print(is_all_different(arr1))
print(is_all_different(arr2))