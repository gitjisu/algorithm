import sys
sys.stdin = open('input.txt')

for tc in range(10):
    n = int(input())
    arr = list(map(int, input().split()))

    total = 0
    for i in range(2, n-2):
        max_value = 0
        for j in (arr[i-2], arr[i-1], arr[i+1], arr[i+2]):
            if j > max_value:
                max_value = j
        if arr[i] > max_value:
            total += arr[i] - max_value

    print(f'#{tc} {total}')


