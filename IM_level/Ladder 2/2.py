import sys
sys.stdin = open('2.txt')
for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    result_cnt = 9999999999
    for i in range(100):
        if arr[0][i] == 1: # 첫번째 줄에서 1인애들 찾기, 찾으면
            cnt = 0
            x,y = i, 0 # x == i y == 0
            while True:
                if x < 99 and arr[y][x+1] == 1: #오른쪽으로가자
                    while x < 99 and arr[y][x+1] == 1:
                        x += 1
                        cnt += 1
                    else:
                        y += 1
                elif x > 0 and arr[y][x-1] ==1:
                    while x > 0 and arr[y][x-1] == 1:
                        x -= 1
                        cnt += 1
                    else:
                        y +=1
                elif arr[y+1][x] == 1:
                    y += 1
                if y == 99:
                    if result_cnt >= cnt:
                        result_cnt = cnt
                        result = i
                    break

    print(f'#{tc} {result}')