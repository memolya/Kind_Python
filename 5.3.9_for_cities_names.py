cities_names_original = input().split()
cities_names_modified = []

for name in cities_names_original:
    if name[-1].lower() in 'ьъы':
        name = name[:-1]  # убираем последнюю букву
        cities_names_modified.append(name.lower())
    else:
        cities_names_modified.append(name.lower())

for i in range(len(cities_names_modified)-1):
    if cities_names_modified[i][-1] != cities_names_modified[i+1][0]:
        print('НЕТ')
        break
else: # конструкция for-else
    print('ДА')

