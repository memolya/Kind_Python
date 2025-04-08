import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

for i, line in enumerate(lst_in):
    cleaned = ' '.join(line.split())
    lst_in[i] = cleaned.replace(' ', '-')

print(*lst_in, sep = '\n')
