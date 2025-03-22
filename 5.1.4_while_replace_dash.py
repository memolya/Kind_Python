text = input()
new_text = ''

i = 0

while i < len(text):
    if text[i] != '-':
        new_text += text[i]
        i += 1
    else:
        while i < len(text) and text[i] == '-':
            i += 1
        new_text += '-'

print(new_text)