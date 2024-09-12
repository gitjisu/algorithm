import sys

n, m = map(int, input().split())


result = []

maze1 = [list(map(int, input().split())) for _ in range(n)]
maze2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n) :
  temp = []
  for j in range(m) :
    temp.append(maze1[i][j] + maze2[i][j])
  result.append(' '.join(map(str, temp)))

print(('\n').join(result))