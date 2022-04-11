import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1, T+1):
    text, pattern = input().split()
    cnt = 0
    i = 0
    while i < len(text) - len(pattern)+1 :
        for j in range(len(pattern)):
            if pattern[j] != text[i+j]:
                i += 1
                break
        else:
            cnt += 1
            i += len(pattern)

    total = len(text) - (len(pattern)*cnt) + cnt

    print(f'#{tc} {total}')