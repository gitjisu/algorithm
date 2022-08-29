import sys
sys.stdin = open('1979.txt')

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    #가로
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0
    #세로
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr)):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == n-1:
                if cnt == k:
                    result += 1
                cnt = 0




                