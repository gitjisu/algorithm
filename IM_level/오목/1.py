import sys
sys.stdin = open('1.txt')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]

    check = 'NO'
    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[i][j] == 'o':
                cnt += 1
        if cnt >= 5:
            check = 'YES'

    for i in range(n):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 'o':
                cnt += 1
        if cnt >= 5:
            check = 'YES'


    l = 0
    for i in range(n):
        if arr[i][i] == 'o':
            l += 1
        if l >= 5:
            check = 'YES'

    r = 0
    for i in range(n):
            if arr[i][n-1-i] == 'o':
                r += 1
            if r >= 5:
                check = 'YES'
    print(check)
