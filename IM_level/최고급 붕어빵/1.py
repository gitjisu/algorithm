import sys
sys.stdin = open('1.txt')
T = int(input())
for tc in range(1, T+1):
    n, m, k = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    # n = 오늘 오는 손님 수
    # m = 붕어빵 만드는데 걸리는 시간
    # k = 만들 수 있는 붕어빵 갯수
    # arr = 각각 손님이 몇초에 오는지?
    # arr(i) = i + 1 번째 손님이 도착한 시간
    # arr[i] 시간의 생산량 = arr[i]//m*k
    # ans = 'Possible'
    # for i in range(n):
    #     if arr[i]//m*k < i + 1:
    #         ans = 'Impossible'
    #         break
    # print(f'#{tc} {ans}')
    cnt = [0] * 1111112
    for x in arr:
        cnt[x] += 1
    for i in range(1, 1111112):
        cnt[i] += cnt[i-1]

    ans = 'Possible'
    for i in range(1111112):
        if cnt[i] > i//m*k :
            ans = 'Impposible'
            break
    print(ans)