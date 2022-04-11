import sys
sys.stdin = open('4836.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    canvas = [[0] * 10 for _ in range(10)]
    purple = 0
    for _ in range(n):
        x1, y1, x2, y2, color = map(int,input().split())
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if color == 1:
                    canvas[i][j] += 1
                if color == 2:
                    canvas[i][j] += 2


    purple = 0
    for i in range(len(canvas)):
        for j in range(len(canvas)):
            if canvas[i][j] == 3:
                purple += 1
    print(f'#{tc} {purple}')



