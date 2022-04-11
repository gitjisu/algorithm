import sys
sys.stdin = open('1.txt')
from collections import deque


def dfs(v):
    dfs_lst[v] = 1
    print(v, end=' ')
    for i in range(len(arr[v])):
        if dfs_lst[i] != 1 and arr[v][i] == 1:
            dfs(i)


def bfs(v):
    bfs_lst[v] = 1
    queue = deque([v])

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in range(len(arr[v])):
            if bfs_lst[i] != 1 and arr[v][i] == 1:
                queue.append(i)
                bfs_lst[i] = 1


T = int(input())
for tc in range(T):
    n, m, v = map(int, input().split())

    arr = [[0] * (n+1) for _ in range(n+1)]
    for i in range(m):
        p, c = map(int, input().split())
        arr[p][c] = 1
        arr[c][p] = 1

    dfs_lst = [0] * (n+1)
    bfs_lst = [0] * (n+1)

    dfs(v)
    print()
    bfs(v)
    print()
