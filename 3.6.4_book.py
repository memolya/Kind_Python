name, author, pages, price = input(), input(), int(input()), float(input())
original_list = [name, author, pages, price]

original_list.pop(original_list.index(pages))
original_list[original_list.index(author)] = 'Пушкин'
original_list[original_list.index(price)] *= 2

print(original_list)
