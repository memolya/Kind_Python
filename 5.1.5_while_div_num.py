num = input()

multipl = 1
i = 0

while i < len(num):
    multipl *= int(num[i])
    i += 1

print(multipl)

# num = input()
# result = 1
#
# for digit in num:
#     result *= int(digit)
#
# print(result)

# from functools import reduce
#
# num = input()
# result = reduce(lambda x, y: x * int(y), num, 1)
#
# print(result)
