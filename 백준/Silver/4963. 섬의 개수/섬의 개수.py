import sys

sys.setrecursionlimit(10**6)

while True:
    input = sys.stdin.readline()
    w, h = map(int, input.split())
    if w == 0 and h == 0:
        break
    else:
        island = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        answer = 0
        def dfs(x, y):
            visited[x][y] = True
            dx = [-1, 1, 0, 0, -1, 1, -1, 1]
            dy = [0, 0, -1, 1, -1, -1, 1, 1]
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if island[nx][ny] == 1 and not visited[nx][ny]:
                        dfs(nx, ny)

        for i in range(h) :
            for j in range(w):
                if island[i][j] == 1 and not visited[i][j]:
                    dfs(i, j)
                    answer += 1

    print(answer)
    



