import sys
sys.stdin = open('input (2).txt')
for tc in range(1, 11):
    tnum = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxV = 0
    for i in range(100):
        sum_row = 0
        for j in range(100):
            sum_row += arr[i][j]
        if maxV < sum_row:
            maxV = sum_row

    for i in range(100):
        sum_column = 0
        for j in range(100):
            sum_column += arr[j][i]
        if maxV < sum_column:
            maxV = sum_column

    sum_diagonalR = 0
    for i in range(100):
        sum_diagonalR += arr[i][i]
    if maxV < sum_diagonalR:
        maxV = sum_diagonalR

    sum_diagonalL = 0
    for i in range(100):
        sum_diagonalL += arr[i][99-i]
    if maxV < sum_diagonalL:
        maxV = sum_diagonalL

    print(f'#{tc} {maxV}')
