cities = list(input().split())
if 'Москва' in cities:
    cities.remove('Москва')
print(*cities)

