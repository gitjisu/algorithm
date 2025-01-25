import sys

sys.setrecursionlimit(10000)
t = int(input())



def dfs(x,y) :
  visited[x][y] = True
  # 상하좌우
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < N and 0 <= ny < M :
      if graph[nx][ny] == 1:
        if visited[nx][ny] == False:
          dfs(nx,ny)
        

  

for _ in range(t) :
  M,N,K = map(int, input().split()) 
  graph = [[0]*M for _ in range(N)]
  visited = [[False]*M for _ in range(N)]
  answer = 0
  for _ in range(K) :
    x, y = map(int, input().split())
    graph[y][x] = 1


  for i in range(N):
    for j in range(M):
      if graph[i][j] == 1 and visited[i][j] == False:
        answer += 1
        dfs(i,j)



  
        
        



  print(answer)


  
