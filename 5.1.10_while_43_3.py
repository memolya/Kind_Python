number = 100
result = []

while number <= 999:
    if number % 47 == 43 and number % 3 == 0:
        result.append(str(number))
    number += 1

print(' '.join(result))
