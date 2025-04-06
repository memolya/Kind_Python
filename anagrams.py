from collections import defaultdict

words = ['вектор', 'кот', 'ток', 'тровек', 'кто', 'векотр', 'пёс', 'спё', 'сеп', 'епс']

anagram_groups = defaultdict(list)
#print(anagram_groups)

for word in words:
    # ключ одинаковый для всех анаграмм одного слова
    # sorted(word) превращает слово в список символов и сортирует их
    # ''.join склеивает список символов обратно в строку
    key = ''.join(sorted(word))
    anagram_groups[key].append(word)

#print(anagram_groups)

result = []
used_keys = set()

for word in words:
    key = ''.join(sorted(word))

    if key not in used_keys:
        result.extend(anagram_groups[key])
        used_keys.add(key)

print(result)