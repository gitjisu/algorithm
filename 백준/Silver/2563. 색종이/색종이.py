import sys


arr = [[0 for j in range(100)] for i in range(100)]

t = int(input())

result = 0

for _ in range(t) :
  x,y = map(int, input().split(' '))

  
  for i in range(100) :
    for j in range(100) :
      if arr[i][j] == 0 :
        if x<=i<x+10 and y<=j<y+10 :
          arr[i][j] = 1
          result += 1
          
print(result)


        