import sys
sys.stdin = open('5432.txt')

tc = int(input())
for t in range(1, tc+1):
    still = input()
    l = still.replace('()', '1')
    print(l)
    # 쇠막대기
    x = 0
    # 잘린거
    c = 0
    for i in l:
        # 쇠막대기 갯수
        if i == '(':
            x += 1
            c += 1
        # 쇠막대기 갯수만큼 ++
        elif i == '1':
            c += x
        # 막대기 갯수 감소
        else:
            x -= 1
    print(f'#{t} {c}')