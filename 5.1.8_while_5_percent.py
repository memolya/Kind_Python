n = int(input())

deposit = 1000
i = 1

while i <= n:
    deposit += deposit*0.05
    i += 1

print(round(deposit, 2))