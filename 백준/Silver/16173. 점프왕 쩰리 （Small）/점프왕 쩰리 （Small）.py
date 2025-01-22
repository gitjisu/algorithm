import sys


def dfs(x,y) :

  # 영역을 벗어났다면 return
  if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] == True :
    return
  
  if graph[x][y] == 0 :
    return
  
  if x == n-1 and y == n-1 :
    global end
    end = True
    return
  
  
  


  # 그게 아니라면 일단 방문했다고 표시
  visited[x][y] = True
  # 그리고 우 또는 하로만 이동 graph[x][y] 만큼
  dfs(x+graph[x][y],y)
  dfs(x,y+graph[x][y])


n = int(input())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]
end = False


dfs(0,0)


if end :
  print('HaruHaru')
else :
  print('Hing')