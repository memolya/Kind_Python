t = ["– Скажи-ка, дядя, ведь не даром",
    "Я Python выучил с каналом",
    "Балакирев что раздавал?",
    "Ведь были ж заданья боевые,",
    "Да, говорят, еще какие!",
    "Недаром помнит вся Россия",
    "Как мы рубили их тогда!"
    ]

# for i in range(len(t)):
#     for ch in remove_chars:
#         t[i] = t[i].replace(ch, '')

# вариант 2
# Используем list comprehension вместо цикла
# t = [line.translate(str.maketrans('', '', "–")) for line in t]
#
# result = [[word for word in line.split(' ') if len(word) > 3] for line in t]
#
# print(result)

lst = [[j for j in i.split() if len(j) > 3] for i in t]
print(lst)