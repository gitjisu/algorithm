import sys
sys.stdin = open('9386.txt')

t = int(input())
for tc in range(t):
    # n = 수열의 길이
    n = int(input())
    nums = list(map(int, input()))

    max = 0
    cnt = 0

    for i in range(n):
        if nums[i] == 1:
            cnt += 1
            if max < cnt:
                max = cnt
        else:
            cnt = 0
    print(f'#{tc+1} {max}')