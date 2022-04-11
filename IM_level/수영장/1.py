import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    total = [0 for _ in range(13)]


    for i in range(1, 13):
        total[i] = min(plan[i] * price[0], price[1])
        if i > 2:
            total[i] =