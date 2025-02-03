a, b, c, d = map(int, input().split())
if (a > c + 1 and b > d + 1
        or a > d + 1 and b > c + 1):
    print('ДА')
else:
    print('НЕТ')