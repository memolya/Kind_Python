import sys

s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
all_valid = True  # Флаг, что все строки валидны

for line, row in enumerate(lst_in):
    #print(lst_in[line], 'a', type(lst_in[line]), f'index - {line}')

    for i, symbol in enumerate(row):
        if symbol == 1:
            # Если текущий элемент равен 1
            has_neighbor_one = False
            # Проверяем левого соседа, если он существует
            if i > 0 and row[i - 1] == 1:
                has_neighbor_one = True
            # Проверяем правого соседа, если он существует
            if i < len(row) - 1 and row[i + 1] == 1:
                has_neighbor_one = True
            # Проверяем диагональ сверху слева
            if line > 0 and i > 0 and lst_in[line - 1][i - 1] == 1:
                has_neighbor_one = True
            # Проверяем диагональ сверху справа
            if line > 0 and i < len(row) - 1 and lst_in[line - 1][i + 1] == 1:
                has_neighbor_one = True
            # Проверяем диагональ снизу слева
            if line < len(lst_in) - 1 and i > 0 and lst_in[line + 1][i - 1] == 1:
                has_neighbor_one = True
            # Проверяем диагональ снизу справа
            if line < len(lst_in) - 1 and i < len(row) - 1 and lst_in[line + 1][i + 1] == 1:
                has_neighbor_one = True
            # Проверяем верх
            if line > 0 and lst_in[line - 1][i] == 1:
                has_neighbor_one = True
            # Проверяем низ
            if line < len(lst_in) - 1 and lst_in[line + 1][i] == 1:
                has_neighbor_one = True

            if has_neighbor_one:
                all_valid = False
                break  # Прерываем цикл по текущей строке

    if not all_valid:
        break  # Прерываем цикл по строкам, если найдена невалидная строка

print("ДА" if all_valid else "НЕТ")