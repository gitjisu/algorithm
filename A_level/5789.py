import sys
sys.stdin = open('5789.txt')

tc = int(input())
for t in range(tc):
    # n = 상자 갯수 q = 횟수
    n, q = map(int, input().split())
    box = [0] * n
    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            box[j] = i + 1

    result = ' '.join(map(str, box))
    print(f'#{t+1} {result}')
