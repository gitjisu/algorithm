import sys
sys.stdin = open('1.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input()) # n*n 배열
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    flag = 'ok'
    stack = []
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                stack.append((i, j))
                visited[i][j] = 1

        while stack:
            x, y = stack.pop()
            if arr[x][y] == 3:
                result = 1
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and (arr[nx][ny] == 0 or arr[nx][ny] == 3):
                    stack.append((nx, ny))
                    visited[nx][ny] = 1

    print(result)