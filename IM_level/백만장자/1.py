import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1,T+1):
    num = int(input())
    arr = list(map(int,input().split()))
    last = arr[-1]
    cnt =
    for i in range(len(arr)-2,-1,-1):
        if last > arr[i]:
            cnt += last-arr[i]
        else:
            last = arr[i]

    print(f'#{tc} {cnt}')