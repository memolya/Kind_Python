cities = list(map(str, input().split()))
result = [c for c in cities if len(c) > 5]
print(*result)