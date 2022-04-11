import sys
sys.stdin = open('1.txt')

power = {'A': 1, 'B': 2, 'C': 3}

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    di = [-1, 1, 0, 0]
    dj = [0,0, -1, 1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'A' or arr[i][j] == 'B' or arr[i][j] == 'C': # 기지국인경우
                for k in range(1, 1+power[arr[i][j]]):
                    for v in range(4):
                        ni = i + di[v] * k
                        nj = j + dj[v] * k
                        if 0 <= ni < n and 0 <= nj < n:
                            arr[ni][nj] = 'X'

    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'H':
                cnt +=1

    print(cnt)


