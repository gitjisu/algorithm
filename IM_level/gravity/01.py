import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    max_gravity = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if boxes[i] > boxes[j]:
                cnt += 1
        if cnt > max_gravity:
            max_gravity = cnt
    print(f"#{tc} {max_gravity}")