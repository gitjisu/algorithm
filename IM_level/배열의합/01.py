import sys
sys.stdin = open('1.txt')

T = int(input())
def perm(idx, temp):
    global result
    if temp > result:
        return
    if idx == n :
        if temp < result
            result = temp
    for i in range(n):
        if not use[i]:
            use[i] = 1
            perm(idx+1, temp+arr[idx][i])
            use[i] = 0

for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result, temp = 100, 0
    use = [0] * n
    perm(0, 0)
    print(f'#{tc} {}')