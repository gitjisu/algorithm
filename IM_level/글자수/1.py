import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = [list(map(str, input())) for _ in range(2)]

    max_count = 0
    for i in range(len(n)):
        count = 0
        for j in range(len(m)):
            if n[i] == m[j]:
                count += 1
        if max_count < count:
            max_count = count
    print(f'#{tc} {max_count}')