import sys


n = int(input())

a = sorted(list(map(int, input().split())))
calc_a = [False] * n
b = list(map(int, input().split()))
sorted_b = sorted(b, reverse=True)


result = 0
for i in range(n) :
  bb = sorted_b[i]
  for j in range(n) :
    if b[j] == bb and calc_a[j] == False:
      calc_a[j] = a.pop(0)
      break

for i in range(n) :
  result += calc_a[i] * b[i]


print(result)
