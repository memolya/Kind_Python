import re

phone = input()

pattern = r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$'

if re.fullmatch(pattern, phone):
    print('ДА')
else:
    print('НЕТ')

