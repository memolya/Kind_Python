desired_km = int(input())
counter_days = 1
total_km = 10

while total_km <= desired_km:
    total_km += total_km*0.1
    counter_days += 1
print(counter_days)