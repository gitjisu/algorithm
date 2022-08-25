import sys
sys.stdin = open('2001.txt')

t = int(input())

for tc in range(1, t+1):
    n, m  = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(n)]
    max_kill = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            kill = 0
            for i2 in range(m): # 0 1
                for j2 in range(m):
                    kill += arr[i+i2][j+j2]
                if kill > max_kill:
                    max_kill = kill

    print(f'#{tc} {max_kill}')



