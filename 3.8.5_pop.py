lst = list(map(int, input().split()))
end = lst.pop()
lst.append(end % 2 != 0)
print(*lst)
