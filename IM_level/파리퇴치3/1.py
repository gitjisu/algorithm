import sys
sys.stdin = open('1.txt')
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    di = [-1, +1, 0, 0] #상하좌우
    dj = [0, 0, -1, +1]
    rc = 0
    for i in range(n):
        for j in range(n):
            center = arr[i][j]
            total = center
            for k in range(1, m):
                for v in range(4):
                    dx = i + di[v] * k
                    dy = j + dj[v] * k
                    if 0 <= dx < n and 0 <= dy < n:
                        total += arr[dx][dy]
            if rc < total:
                rc = total

    ci = [-1, -1, 1, 1]
    cj = [-1, 1, 1, -1]
    cross = 0
    for i in range(n):
        for j in range(n):
            center = arr[i][j]
            total = center
            for k in range(1, m):
                for v in range(4):
                    ix = i + ci[v] * k
                    jy = j + cj[v] * k
                    if 0 <= ix < n and 0 <= jy < n:
                        total += arr[ix][jy]
            if cross < total:
                cross = total
    if cross < rc:
        print(f'#{tc} {rc}')
    else:
        print(f'#{tc} {cross}')




