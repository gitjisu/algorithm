import sys
sys.stdin = open('1961.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    first = [[0] * n for _ in range(n)]
    second = [[0] * n for _ in range(n)]
    third = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            first[i][j] = arr[n-1-j][i]
            second[i][j] = arr[n-1-i][n-1-j]
            third[i][j] = arr[j][n-1-i]
    print(f'#{tc}')
    for a1, a2, a3 in zip(first, second, third):
        print(f'{"".join(map(str, a1))} {"".join(map(str, a2))} {"".join(map(str, a3))}')