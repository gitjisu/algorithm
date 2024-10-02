import sys


n = int(input())
arr = map(int, input().split())
result = 0

for m in arr :  
    temp = []
    if m == 1:
        continue
    for i in range(1, m+1) :
        if m % i == 0 :
            temp.append(i)

    if temp[0] == 1 and temp[1] == m :
        result += 1


print(result)