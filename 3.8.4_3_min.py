num = list(map(int, input().split()))
three_min = []
for i in range(3):
    mn = min(num)
    three_min.append(mn)
    num.remove(mn) # remove вместо pop,
                   # pop удалял бы элемент с индексом, к-й равен mn, а не сам mn
                   # pop удаляет эл-т по индексу, remove - по значению

three_min = sorted(three_min)
print(*three_min)

