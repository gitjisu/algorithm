import sys
sys.stdin = open('1.txt')

T = int(input())
for tc in range(1,T+1):
    text, pattern = input().split()
    len_t = len(text)
    len_p = len(pattern)

    i = 0
    total = 0
    while i < len_t:
        if text[i] == pattern[0]:
            if text[i:i+len_p] == pattern:
                i += len_p
            else:
                total += 1
                i += 1
        else:
            total += 1
            i += 1
    print(f'#{tc} {total}')
