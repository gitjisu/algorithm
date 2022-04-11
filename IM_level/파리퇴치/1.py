import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    for i in range(n-m+1): # 0 1 2 3 4
        for j in range(n-m+1): # 0 1 2 3 4
            row = 0
            column = 0
            l = 0
            r = 0
            for i2 in range(m): # 0 1
                for j2 in range(m): # 0 1
                    row += arr[i+i2][j+j2]
                    column += arr[j+j2][i+i2]
                    l += arr[i+j2][m-j2-1]
                    r += arr[i+i2][i+i2]

    print(f'#{tc}{max_v}')