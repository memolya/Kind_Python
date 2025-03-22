n = int(input())

x = 2
res = 1

while x <= n:
    res += 1 / x
    x += 1

print(round(res, 3))

# n = int(input())
#
# res = 0
#
# for i in range(1, n + 1):
#     res += 1 / i
#
# print(round(res, 3))
