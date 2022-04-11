import sys
sys.stdin = open('1.txt')

dx = [0,0,1,-1]
dy = [1,-1,0,0]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    stack = []
    result = 0
    for i in range(n):
        for j in range(n):
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
    print(f'#{tc} {result}')