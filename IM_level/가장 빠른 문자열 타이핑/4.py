import sys
sys.stdin = open('1.txt')

T = int(input())

for tc in range(1, T+1):
    a,b = input().split()

    idx = cnt = 0
    while idx < len(a):
        if a[idx:idx+len(b)] == b:
            idx += len(b)
        else:
            idx += 1
            cnt += 1
    print(f'#{tc} {cnt}')