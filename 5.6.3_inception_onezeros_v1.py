import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
all_valid = True  # Флаг, что все строки валидны

# Направления: (dx, dy) — смещение по строкам (line) и столбцам (i)
directions = [(-1, -1), (-1, 0), (-1, 1), # Вверх-влево, Вверх, Вверх-вправо
              (0, -1),           (0, 1),  # Влево,     , Вправо
              (1, -1),   (1, 0), (1, 1)]  # Вниз-влево, Вниз, Вниз-вправо

rows, cols = len(lst_in), len(lst_in[0])

for line in range(rows):
    for i in range(cols):
        if lst_in[line][i] == 1:
            for dx, dy in directions:
                nx, ny = line + dx, i + dy
                if 0 <= nx < rows and 0 <= ny < cols and lst_in[nx][ny] == 1:
                    all_valid = False
                    break #Нашли соседа с 1, выходим из направлений
            if not all_valid:
                break # Выходим из текущей строки
        if not all_valid:
            break # Прерываем цикл по строкам



print("ДА" if all_valid else "НЕТ")