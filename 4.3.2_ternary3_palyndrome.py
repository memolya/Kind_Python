text = input().lower()

msg = 'палиндром' if text[::] == text[::-1] else 'не палиндром'

print(msg)

