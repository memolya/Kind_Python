text = input().split()
l = len(text[1])
#  первое слово обрезать до длины второго
first_word_cut = text[0][:l]
# у каждого слова выделить символы с нечетными индексами и полученные слова сравнить
first_word_odd = first_word_cut[1::2]
second_word_odd = text[1][1::2]
print(first_word_odd == second_word_odd)