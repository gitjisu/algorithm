import sys
from collections import deque


def dfs(index) :
  # 방문처리
  dfs_visited[index] = True
  dfs_answer.append(index)
  # 인접한 노드들을 탐색
  for i in sorted(dfs_graph[index]) :
    if not dfs_visited[i] :
      dfs(i)

  

def bfs(index) :
  # 시작 노드를 큐에 담는다
  queue = deque([index])
  # 방문처리를 해준다
  bfs_visited[index] = True
  # 방문한거 정답에 넣어주기
  bfs_answer.append(index)

  while queue :
    # 큐에서 하나 꺼내기
    current = queue.popleft()
    # 인접한 노드들을 탐색
    for next in sorted(bfs_graph[current]) :
      if not bfs_visited[next] :
        # 큐에 추가
        queue.append(next)
        
        # 방문처리
        bfs_visited[next] = True
        # 정답에 추가
        bfs_answer.append(next)





n, m, v = map(int, input().split())
dfs_graph = [[] for _ in range(n + 1)]
dfs_visited = [False] * (n + 1)
dfs_answer = []

bfs_graph = [[] for _ in range(n + 1)]
bfs_visited = [False] * (n + 1)
bfs_answer = []

for _ in range(m) :
  a, b = map(int, input().split())
  dfs_graph[a].append(b)
  dfs_graph[b].append(a)
  bfs_graph[a].append(b)
  bfs_graph[b].append(a)

dfs(v)
bfs(v)

print((" ").join(map(str, dfs_answer)))
print((" ").join(map(str, bfs_answer)))
