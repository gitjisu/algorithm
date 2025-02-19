import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력 적용

def bfs(start):
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while queue:
        current = queue.popleft()
        
        for nxt in graph[current]:
            if not visited[nxt]:
                visited[nxt] = True
                distance[nxt] = distance[current] + 1
                queue.append(nxt)

# 입력
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS 수행
bfs(x)

# 결과 출력 (거리 k인 도시)
found = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        found = True

if not found:
    print(-1)
