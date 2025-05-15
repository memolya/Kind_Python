# 1, 2, 4, 8, 16, 32 и 64

num = int(input())
nominal = [64, 32, 16, 8, 4, 2, 1]
result = []

while num != 0:
    for i in nominal: # перебираем номиналы
        while num // i >= 1: # пока целочисленно делится на номинал
            result.append(i)
            num -= i # вычитаем уже готовый размен

print(*result)