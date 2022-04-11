T = int(input())

for ts in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split())) # 1 5 3
    B =list(map(int, input().split()))  # 3 6 -7 5 4

    if N > M:
        N, M = M, N
        A, B = B, A

    ans = 0
    for i in range(M - N + 1): # 0 1 2
        a = 0
        for j in range(N): # 0 1 2
            a += A[j] * B[j + i]
        if ans < a:
            ans = a

    print(f'#{ts+1} {ans}')