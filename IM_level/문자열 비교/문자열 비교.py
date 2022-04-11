import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())

for tc in range(1, T+1):
    n = input()
    m = input()
    result = 0
    for i in range(len(m)-len(n)+1):
        if m[i:i+len(n)] == n:
            result = 1

    print(f'#{tc} {result}')