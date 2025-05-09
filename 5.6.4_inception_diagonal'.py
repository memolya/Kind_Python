import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]
all_valid = True

rows, cols = len(lst_in), len(lst_in[0])

for line in range(rows):
    for idx in range(cols): # проходим по элементам строки и по столбцу одновременно
        num_line = lst_in[line][idx] # элемент строки с индексом idx
        num_col = lst_in[idx][line] # элемент столбца с индексом line (читаем по строкам)

        #print(f"Сравниваем строка[{line}][{idx}] = {num_line} и столбец[{idx}][{line}] = {num_col}")

        if num_line != num_col:
            all_valid = False
            break

    if not all_valid:
        break

print("ДА" if all_valid else "НЕТ")


