import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    a = a.replace(b, "!")
    print(f'#{tc} {len(a)}')