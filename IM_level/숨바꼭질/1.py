import sys
sys.stdin = open('1.txt')
from collections import deque




n, k = map(int, input().split())
MAX = 100001
visited = [0] * MAX

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for dx in [x-1, x+1, x*2]:
            if 0 <= dx < MAX and visited[dx] == 0:
                visited[dx] = visited[x] + 1
                q.append(dx)

bfs()

