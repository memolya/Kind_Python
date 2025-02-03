text = input()
if text[:].casefold() == text[::-1].casefold():
    print('ДА')
else:
    print('НЕТ')