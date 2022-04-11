import sys
sys.stdin = open('1.txt')

def f(N):
    if N % 10 == 0 : # 10의배수이면
        if N == 10:  # 10일때 1가지
            return 1
        elif N == 20: # 20일때 3가지
            return 3
        else:
            return f(N-10) + (2*f(N-20)) # 1, 3, 5, 11, 21... (점화식 (n-10) + (2*n-20)
T = int(input())
for tc in range(1, T+1):
    d = int(input())
    cnt = f(d)
    print(f'#{tc} {cnt}')