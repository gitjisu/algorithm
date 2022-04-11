import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str,input()))for _ in range(5)]

    max_len = 0
    for i in range(5):
        if max_len < len(arr[i]):
            max_len = len(arr[i])

    new_Arr = [[0]*max_len for i in range(5)]


    for i in range(5):
        for j in range(len(arr[i])):
            new_Arr[i][j] = arr[i][j]

    result = ''
    for i in range(max_len):
        for j in range(5):
            if new_Arr[j][i] != 0:
                result += new_Arr[j][i]
    print(f'#{tc} {result}')