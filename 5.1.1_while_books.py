price = float(input())
quantity = 2

while quantity <= 10:
    print(round(price*quantity, 1), end = ' ')
    quantity += 1