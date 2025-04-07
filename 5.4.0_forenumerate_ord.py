text = input()
indexes = []

for i, _ in enumerate(text[:-1]):  # до предпоследнего символа, чтобы не выйти за границы
    if text[i:i+2] == "ра":
        indexes.append(i)

if indexes:
    print(*indexes)
else:
    print(-1)
