import sys
sys.stdin = open('1.txt')
from collections import deque

def bfs(arr, v, bfs_lst):
    global cnt
    bfs_lst[v] = 1
    q = deque([v])

    while q:
        v = q.popleft()
        cnt += 1
        for i in range(len(arr[v])):
            if bfs_lst[i] != 1 and arr[v][i] == 1:
                q.append(i)
                bfs_lst[i] = 1


n = int(input())
m = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    p, c = map(int, input().split())
    arr[p][c] = 1
    arr[c][p] = 1

bfs_lst = [0] * (n+1)
cnt = -1
v = 1

bfs(arr, v, bfs_lst)
print(cnt)
