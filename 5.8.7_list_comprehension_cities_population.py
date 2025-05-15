cities_and_population = list(map(str, input().split()))

cities = [i for i in cities_and_population if i.isalpha()]
population = [int(x) for x in cities_and_population if x.isdigit()]

result = [[cities[z], population[z]] for z in range(len(cities))]
print(result)