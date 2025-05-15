num = int(input())

# Внешний цикл: for i in range(num) — строки
# Внутренний цикл: for j in range(num) — столбцы

lst = [[1 if i == j else 0 for j in range(num)] for i in range(num)]

for row in lst:
    print(*row)

# num = int(input())
#
# matrix = []
#
# for i in range(num):
#     row = []
#     for j in range(num):
#         if i == j:
#             row.append(1)  # Главная диагональ
#         else:
#             row.append(0)  # Остальные элементы
#     matrix.append(row)
#
# # Вывод таблицы
# for row in matrix:
#     print(*row)
