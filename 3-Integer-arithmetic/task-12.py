n = int(input())
fd = n // 1000
sd = n // 100 % 10
td = n % 100 // 10
ld = n % 10

ad = fd - ld
bc = sd - td

print((ad ** 2 + bc ** 2) + 1)
