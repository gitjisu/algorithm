import sys
sys.stdin = open('새 텍스트 문서.txt')
T = int(input())
for tc in range(1, T+1):
    still = input()
    l = still.replace('()', 'l')
    x = 0
    c = 0
    for i in l:
        if i == '(':
            x += 1
            c += 1
        elif i == 'l':
            c += x
        else:
            x -= 1

    print(f'#{tc} {c}')
