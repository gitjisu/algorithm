import sys
sys.stdin = open('새 텍스트 문서.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(str, input()))for _ in range(5)]

    max_value = 0
    for i in range(len(arr)):
        if max_value < len(arr[i]):
            max_value = len(arr[i])

    result = ' '
    for i in range(max_value): #6
        for j in range(5): #5
            if i < len(arr[j]):
                result += arr[j][i]

    print(f'#{tc} {result}')
