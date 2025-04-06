n = int(input())

if n < 2:
    print('НЕТ')
else:
    for i in range(2, n): # для 2 будет пустой диапазон
        if n % i == 0:
            print('НЕТ')
            break
    else:
        print('ДА')
