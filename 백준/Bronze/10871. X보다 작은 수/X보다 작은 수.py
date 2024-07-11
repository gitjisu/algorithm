import sys


result = ''

n, x = map(int, input().split())
tc = input().split()

for i in range(0, n):
  if int(tc[i]) < x :
    result += tc[i] + ' '

print(result)

