from math import sqrt
from collections import deque

nums = deque(map(int, input().split()))
# длина цикла для внешнего и внутреннего списка -
# √len(nums) (напр. 2 вложенных цикла по 2 символа)
length = int(sqrt(len(nums)))

# Внешний цикл for _ in range(length) - количество подсписков, которые будут в result
# 1 итерация - 1 вложенный список
# Внутренний цикл for _ in range(length) - lenghth элементов для каждого вложенного списка
# При каждом проходе удаляет элемент из
# начала очереди nums с помощью .popleft() и добавляет его в текущий подсписок.
result = [[nums.popleft() for _ in range(length)] for _ in range(length)]
print(result)