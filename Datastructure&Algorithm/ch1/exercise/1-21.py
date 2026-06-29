arr = []
while(True):
    try:
        str = input()
        arr.append(str)
    except:
        for i in range(-1, -len(arr) - 1, -1):
            print(arr[i])
