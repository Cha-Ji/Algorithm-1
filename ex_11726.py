a, b = 1, 1
for i in range(2, int(input()) + 1):
    a, b = b, a + b

print(b % 10007)