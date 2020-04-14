from itertools import dropwhile

lst = [0, 2, 4, 12, 18, 13, 14, 22, 23, 44]

result = list(dropwhile(lambda x:x%2==0, lst))

print(result)
