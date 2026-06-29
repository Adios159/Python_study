def multiple_array(arr1, arr2):
    if(len(arr1) != len(arr2)):
        return False
    ans = [arr1[i] * arr2[i] for i in range(0, len(arr1))]
    return ans

arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 3, 4, 5, 6]
print(multiple_array(arr1, arr2))