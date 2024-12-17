a, b, c = map(int, input().split())
print(a + b > c and a + c > b and c + b > a)