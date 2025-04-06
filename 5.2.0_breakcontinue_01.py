p = [0] * 10

counter = 0
user_number = 0

while counter < 5:
    user_number = int(input())

    if p[user_number] == 1:
        continue # если уже стоит 1 — просим снова

    p[user_number] = 1
    counter += 1 # только когда успешно поставили 1

print(*p)