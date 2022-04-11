import sys
sys.stdin = open('1.txt')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    home = [list(map(str, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            try:
                if home[i][j] == 'A':
                    home[i][j-1] = 'X'
                    home[i][j+1] = 'X'
                    home[i+1][j] = 'X'
                    home[i-1][j] = 'X'
                if home[i][j] == 'B':
                    home[i][j-1] = 'X'
                    home[i][j+1] = 'X'
                    home[i+1][j] = 'X'
                    home[i-1][j] = 'X'
                    home[i][j - 2] = 'X'
                    home[i][j + 2] = 'X'
                    home[i + 2][j] = 'X'
                    home[i - 2][j] = 'X'
                if home[i][j] == 'C':
                    home[i][j-1] = 'X'
                    home[i][j+1] = 'X'
                    home[i+1][j] = 'X'
                    home[i-1][j] = 'X'
                    home[i][j - 2] = 'X'
                    home[i][j + 2] = 'X'
                    home[i + 2][j] = 'X'
                    home[i - 2][j] = 'X'
                    home[i][j - 3] = 'X'
                    home[i][j + 3] = 'X'
                    home[i + 3][j] = 'X'
                    home[i - 3][j] = 'X'
            except IndexError:
                pass

    home_cnt = 0
    for i in range(len(home)):
        for j in range(len(home)):
            if home[i][j] == 'H':
                home_cnt += 1
    print(f'#{tc} {home_cnt}')
