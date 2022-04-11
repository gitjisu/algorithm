import sys
sys.stdin = open('1.txt')

t = int(input())
for tc in range(1, t+1):
    doc = int(input())
    t_list = [list(map(int, input().split()))for _ in range(doc)]
    t_list.sort(key=lambda x:x[1], reverse=True)
    print(t_list)
    quicker_end = t_list.pop()[1] # 제일 빨리 끝나는 시간
    result = 1
    while t_list:
        s, e = t_list.pop()
        if quicker_end <= s:
            quicker_end = e
            result += 1
    print(f'#{tc} {result}')

