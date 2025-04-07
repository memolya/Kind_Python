n = str(input())
it = iter(n)

for i, n in enumerate(n):
    ch = next(it)
    print(ch, end=' ')