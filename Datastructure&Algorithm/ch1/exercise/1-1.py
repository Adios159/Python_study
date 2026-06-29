def is_multiple(a, b):
    if a % b == 0:
        return True
    else:
        return False

a = int(input())
b = int(input())
print(is_multiple(a, b))
