num = int(input())
# Внешний цикл: for i in range(num) — строки
# Внутренний цикл: for j in range(num) — столбцы
result = [[i for j in range(num)] for i in range(num)]
for row in result:
    print(*row)