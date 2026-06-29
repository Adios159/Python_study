def is_even(a):
    temp = 0
    while(True):
        a -= 2
        temp = a
        if(a == 0):
            return True
        elif(a == 1):
            return False
        else:
            continue

a = int(input())
print(is_even(a))

