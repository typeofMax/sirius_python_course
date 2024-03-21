a, b = int(input()), int(input())

c = a // b
d = (c - 1) // (c + 1) + 1
print(d * a + (1 - d) * b)