import sys


arr = [list(map(int, input().split(' '))) for _ in range(9)]

max_num = 0
r,c = 0, 0


for i in range(9) :
  for j in range(9) :
    if (arr[i][j]) > max_num :
      max_num = arr[i][j]
      r,c = i, j

print(max_num)

print(r+1, c+1)