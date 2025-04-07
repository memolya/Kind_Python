# text = input()
#
# for i, l in enumerate(text):
#     if l != ' ':
#         print(l, end='')
#     else:
#         break

# решение с явным итератором
text = input()
it = iter(text)  # создаём итератор вручную

while True:
    ch = next(it)
    if ch == ' ':
        break
    print(ch, end='')
