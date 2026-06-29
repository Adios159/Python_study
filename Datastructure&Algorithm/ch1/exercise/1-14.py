def have_odd_result(arr):
    a = 0
    b = 0
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            a = arr[i]
            b = arr[j]
            if((a * b) % 2 == 1):
                return True
    return False

arr1 = [2, 4, 6, 8, 10]
arr2 = [1, 2, 3, 4, 5]
print(have_odd_result(arr1))
print(have_odd_result(arr2))