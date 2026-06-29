def change_value(arr):
    while(True):
        try:
            idx = int(input("index: "))
            val = int(input("value: "))
            arr[idx] = val
            print(arr)
        except IndexError:
            print("Don`t try buffer overflow attacks in Python!")
            break

arr = [1, 2, 3, 4, 5, 6]
change_value(arr)