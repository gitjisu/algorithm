import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())

for tc in range(1, T+1):
    N = set(list(input()))
    M = input()
    str_cnt = {}
    max_val = 0

    for n in N:
        for m in M:
            if n == m:
                if n in str_cnt:
                    str_cnt[n] += 1
                else:
                    str_cnt[n] = 1

    for value in str_cnt.values():
        if value > max_val:
            max_val = value

    print(f'#{tc} {max_val}'-)
