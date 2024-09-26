import sys
n,m = map(int, input().split(' '))
result = []

i = 1
while True :
  if i > n :
    break
  elif n % i == 0 :
    result.append(i)
  
  i += 1


if len(result) < m :
  print(0)
else :
  print(result[m-1])