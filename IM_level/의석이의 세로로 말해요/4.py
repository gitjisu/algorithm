import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input()))for _ in range(5)]

    max_len = 0
    for i in arr:
        if len(i) > max_len:
            max_len = len(i)

    print(