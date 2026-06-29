def reverse(arr):
    ans = []
    for i in range(-1, -len(arr) - 1, -1):
        ans.append(arr[i])
    return ans

arr = []
for i in range(0, 9):
    arr.append(i)

print(arr)
arr2 = reverse(arr)
print(arr2)