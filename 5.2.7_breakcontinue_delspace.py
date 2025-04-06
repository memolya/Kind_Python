import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)

counter = 0

while counter < len(lst_in):
    if ' ' not in lst_in[counter]:
        print(lst_in[counter], end=' ')
    counter += 1
