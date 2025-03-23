n, m = map(int, input().split())

if n % 2 == 0:
    n += 1  # если n чётное — начинаем с ближайшего нечётного

while n <= m:
    print(n, end=' ')
    n += 2
