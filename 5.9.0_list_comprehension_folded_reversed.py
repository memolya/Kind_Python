import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s if x.strip()]

# Перебираем строки в обратном порядке - for row in lst_in[::-1]
# Перебираем элементы строки тоже в обратном порядке - for x in row[::-1]
result = [x for row in lst_in[::-1] for x in row[::-1]]
print(*result)