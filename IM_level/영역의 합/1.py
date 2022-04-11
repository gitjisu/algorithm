import sys
sys.stdin = open('01.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0] * (N+2)]
    arr += [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    arr += [[0] * (N+2)]
    print(arr)

    sum_value = -999999

    temp1 = 0
    if N < 3:
        sum_value = 0
    # 정사각형 4이상부터
    for i in range(1, N-1):
        for j in range(1, N-1):
            temp = 0
            for i2 in range(3):
                for j2 in range(3):
                    temp += arr[i2 + i][j2 + j]
            if sum_value < temp:
                sum_value = temp

    # 4방향 구하기
    for i in range(len(arr)):
        for j in range(len(arr)):
            if N == 1:
                sum_value = N
            center = arr[i][j]
            total = 0
            total += center
            if N != 1:
                for c in range(1, center):
                    if center == 1:
                        sum_value = 1
                        break
                    try:
                        total += (arr[i+c][j] + arr[i-c][j] + arr[i][j-c] + arr[i][j+c])
                    except IndexError:
                        pass
                if sum_value < total:
                    sum_value = total

    print(sum_value)