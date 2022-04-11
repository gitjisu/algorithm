import sys
sys.stdin = open('1.txt')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
def dfs(a, b):
    global flag
    if arr[a][b] == 3:
        flag = 1
        return

    visited[a][b] = 1
    stack = [[a, b]]

    while stack:
        ii, jj = stack.pop()
        for i in range(4):
            nx = dx[i] + ii
            ny = dy[i] + jj
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
                visited[nx][ny] = 1
                dfs(nx, ny)






t = int(input())
for tc in range(1, t+1):
    n = int(input()) # n*n 배열
    arr = [list(map(int, input())) for _ in range(n)]
    x = y = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                x, y = i, j

    flag = 0

    visited = [[0] * n for _ in range(n)]

    dfs(x, y)
    print(flag)
