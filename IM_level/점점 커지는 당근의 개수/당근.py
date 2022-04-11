import sys
sys.stdin = open('당근.txt')

T = int(input())
for tc in range(1, T+1):
    carrot = int(input())
    size = list(map(int, input().split()))

    cnt = 1
    max_v = 1
    for i in range(1, len(size)):
        if size[i-1] < size[i]:
            cnt += 1
            if max_v < cnt:
                max_v = cnt
        else :
            cnt = 1
    print(f'#{tc} {max_v}')




