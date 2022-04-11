import sys
sys.stdin = open('1.txt')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    card = list(input().split())

    # total = ''
    # for i in range(n//2): # 절반 나누기
    #     total += card[i]+ ' ' +card[i+n//2+n%2] + ' '
    # if n%2 :
    #     total += card[n//2] # 홀수이면..
    # print(f'#{tc} {total}')
    #

    #광용님꺼
    print(f'#{tc}', end=' ')
    for i in range(n//2):
        print(card[i], end=' ')
        if i + (n+1)//2 < n:
            print(card[i+(n+1)//2], end=' ')
    print()
