import sys
sys.stdin = open('1.txt')

def dfs(v, visited):
    for i in lst[v]:
        if visited[i] == 0:
            result.append(i)
            visited[i] = 1
            dfs(i, visited)
T = int(input())
for tc in range(T):
    n, m, v = map(int, input().split())
    lst = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
    # for i in range(len(lst)):
    #     lst[i].sort()
    print(lst)

    result = [v]
    visited[v] = 1
    dfs(v, visited)
    print(*result)