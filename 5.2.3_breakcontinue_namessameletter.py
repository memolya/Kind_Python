names = input().split()
i = 0

while i < len(names):
    if names[i][0].casefold() == names[i][-1].casefold(): # либо names = input().lower().split()
        print('ДА')
        break
    i += 1
else: #Если просто поместить print('НЕТ') после цикла, он всегда выполнится, независимо от того, был break или нет.
    print('НЕТ')