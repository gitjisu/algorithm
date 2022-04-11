import sys
sys.stdin = open('1.txt')
T = int(input())
# 1 -> 0 , 0 -> 1 = toggle
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for k in range(1, m+1):
        if m % k == 0:
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if arr[i-1][j-1] == 0:
                        arr[i-1][j-1] = 1
                    else:
                        arr[i-1][j-1] = 0
        else:
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if (i+j) % k == 0:
                        if arr[i - 1][j - 1] == 0:
                            arr[i - 1][j - 1] = 1
                        else:
                            arr[i - 1][j - 1] = 0
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                cnt += 1

    print(cnt)