import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    max_v = 0
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            cnt = 0
        elif arr[i] == 1:
            cnt += 1
        if max_v < cnt:
            max_v = cnt
    print(f'#{tc} {max_v}')