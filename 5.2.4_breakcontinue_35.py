n = int(input())

i = 0
lst = list(range(1, n+1))
result = []

if n < 100:
    while i < len(lst):
        if lst[i] % 3 == 0 and lst[i] % 5 == 0:
            result.append(lst[i])
        i += 1 # увеличиваем только один раз, вне if
    print(*result)
    
else:
    print('слишком большое значение n')
