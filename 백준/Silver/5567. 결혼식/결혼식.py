import sys
from collections import deque

def bfs(now, distance) :
  queue = deque([{now:distance}])
  visited[now] = True
  global result
  while queue :
    current = queue.popleft()
    
    n = list(current.keys())[0]
    d = list(current.values())[0]
    if d == 2 :
      break
    for i in graph[n] :
      if not visited[i] :
        visited[i] = True
        result += 1
        queue.append({i:d+1})
  return

# 친구수
n = int(input())
# 리스트 길이
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
visited[1] = True
friends = []
result = 0

for _ in range(m):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)


bfs(1, 0)
  

print(result)
