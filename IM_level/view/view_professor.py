import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())  # len(arr)
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(2, N-2):
        # 현재위치와 좌우 2칸씩 차의 최솟값
        min_value = 47984729
        for j in range(5):
            if j != 2:
                if arr[i] - arr[i - 2 + j] < min_value:
                    min_value = arr[i] - arr[i - 2 + j]
        if min_value > 0:
            ans += min_value

    print('#{} {}'.format(tc, ans))