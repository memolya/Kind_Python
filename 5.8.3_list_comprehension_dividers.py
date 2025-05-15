num = int(input())
lst = list(range(1, num+1))
result = [n for n in lst if num % n == 0]
print(*result)