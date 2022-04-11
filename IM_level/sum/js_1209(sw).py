import sys
sys.stdin = open('input (2).txt')

T = 10
n = 100
for tc in range(1, T+1):
    no = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_value = 0

    for i in range(n):
        total = 0
        for j in range(n):
            total += arr[i][j]
        if max_value < total:
            max_value = total

    for i in range(n):
        total = 0
        for j in range(n):
            total += arr[j][i]
        if max_value < total:
            max_value = total

    total = 0
    for i in range(n):
        total += arr[i][i]
        if max_value < total:
            max_value = total

    total = 0
    for i in range(n):
        total += arr[i][n-1-i]
        if max_value < total:
            max_value = total

    print(f'#{tc} {max_value}')