import sys
sys.stdin = open('고대유적.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(n)]
    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    for i in range(m):
        cnt = 0
        for j in range(n):
            if arr[j][i] == 1:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    print(f'#{tc} {max_cnt}')
