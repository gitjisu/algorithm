import sys


while True :
  n = int(input())
  result = []

  
  if n == -1 :
    break
  else :
    i = 1
    for i in range(n) :
      i += 1
      if n%i == 0 and i != n:
        result.append(i)
      
      
  temp = 0
  for i in result:
    temp += i
  
  if temp == n :
    print(f'{n} =', (' + ').join(map(str, result)))
  else:
    print(f'{n} is NOT perfect.')
      