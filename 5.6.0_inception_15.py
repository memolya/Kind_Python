number = int(input())

for i in range(number):
    for j in range(number-1):
            print(1, end = ' ')
    print(5, end = '\n') # вызывается один раз после завершения внутреннего for,
    # то есть один раз на каждую итерацию внешнего цикла (то есть один раз на каждую строку).