cities = list(map(str, input().split()))
result = []

for i in range(len(cities)):
    result.append(len(cities[i]))

print(*result)