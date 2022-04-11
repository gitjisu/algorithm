import sys
sys.stdin = open('6190.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input()) #6480
    num_lst = [2, 3, 5, 7, 11]
    cnt = [0] * 5

    for i in range(len(num_lst)):
        while True: #무한루프
            if n % num_lst[i] == 0:
                n = n//num_lst[i]
                cnt[i] += 1
            else: # 나머지가 0이 아니면 while문 빠져 나가기
                break

    result = ' '.join(map(str, cnt))
    print(f' #{tc} {result}')