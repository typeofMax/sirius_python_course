k, n = int(input()), int(input())
page = (n - 1) // k + 1
line_on_page = ((n - 1) % k) + 1
print(page, line_on_page)
