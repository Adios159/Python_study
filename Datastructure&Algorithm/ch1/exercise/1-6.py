x = int(input())
ans = 0
for i in range(0, x):
    if(i % 2 == 1):
        ans += i ** 2

print(ans)