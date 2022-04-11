import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    num = list(map(int, input().split()))

    num_sum = 0
    for i in range(M):
        num_sum += i
    min_sum = num_sum
    max_sum = num_sum

    for i in range(1, N-M+1):
        num_sum = num_sum - num[i-1] + num[i+M-1]

        if num_sum < min_sum:
            min_sum = num_sum
        elif num_sum > max_sum:
            max_sum = num_sum

    print(f'#{tc} {max_sum - min_sum}')