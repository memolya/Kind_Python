cities = input().split()
i = 0

while i < len(cities):
    if len(cities[i]) <= 5:
        print('НЕТ')
        break
    i += 1
else:
    print('ДА')



