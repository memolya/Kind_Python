n = int(input())
result = []

for number in range(2, n):
    is_prime = True

    for divisor in result: # проверка деления на числа, ранее добавленные в список
        if number % divisor == 0:
            is_prime = False
            break

    if is_prime: # штатное завершение цикла for divior in result
        result.append(number)

print(*result)
