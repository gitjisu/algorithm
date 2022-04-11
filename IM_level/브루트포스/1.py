import itertools
lst = [1,2,3,4,5]
result = itertools.permutations(lst)
for i in result:
    print(i)