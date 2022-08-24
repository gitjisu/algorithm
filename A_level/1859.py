import sys
sys.stdin = open('1859.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    stuff = list(map(int, input().split()))
    result = 0
    max_value = stuff[-1]
    for i in range(n-1, -1, -1):
        # i번째 가격이 max_value보다 크거나 같으면 max_value = i로 초기화
        if stuff[i] >= max_value:
            max_value = stuff[i]
        # 크거나 같은게 나올때까지. result에 차익 더해주기
        result += max_value - stuff[i]
    print(f'#{tc} {result}')
