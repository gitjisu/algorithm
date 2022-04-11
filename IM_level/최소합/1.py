import sys
sys.stdin = open('1.txt')

def BFS(x, y):
    global min_total, sub_sum
    if min_total < sub_sum:
        return
    if x == N - 1 and y == N - 1:
        if min_total > sub_sum:
            min_total = sub_sum
    dx, dy = [1, 0], [0, 1]
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            sub_sum += maze[nx][ny]
            BFS(nx, ny)
            visited[nx][ny] = False
            sub_sum -= maze[nx][ny]



T = int(input())
for idx in range(T):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]
    min_total = 260
    sub_sum = maze[0][0]
    visited = [[False] * N for i in range(N)]
    BFS(0, 0)
    print(f"#{idx + 1} {min_total}")