import sys


r, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(c)] # 이제 열을 바탕으로 리스트를 만든다
visited = [[False] * r for _ in range(c)] # 마찬가지로 c는 행, r은 열로 바꿔야 돼

def dfs(x, y):
    if x == c-1 and y == r-1:
        return True
    
    visited[x][y] = True
    dx = [0, 1] # x는 행(세로)로
    dy = [1, 0] # y는 열(가로)로

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < c and 0 <= ny < r and graph[nx][ny] == 1:
            if not visited[nx][ny]:
                if dfs(nx, ny):
                    return True
    return False

if dfs(0, 0):
    print("Yes")
else:
    print("No")