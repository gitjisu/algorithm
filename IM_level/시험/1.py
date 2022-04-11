import sys
sys.stdin = open('1.txt')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    position = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                position.append(i)
                position.append(j)
    di = [-1, 1, 0, 0] #상하좌우
    dj = [0, 0, -1, 1]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == position[0] and j == position[1]:
                cnt = 0
                for k in range(4):
                    for v in range(n):
                        ni = i + di[k] * v
                        nj = j + dj[k] * v
                        if 0 <= ni < n and 0 <= nj < n:
                            if arr[ni][nj] == 1:
                                break
                            if arr[ni][nj] == 0:
                                cnt += 1
    zero_cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                zero_cnt += 1
    print(f'#{tc} {zero_cnt - cnt}')