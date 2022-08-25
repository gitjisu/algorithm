import sys
sys.stdin = open('5356.txt')

t = int(input())
for tc in range(1, t+1):
    arr = []
    for i in range(5):
        arr.append(list(map(str, input())))

    max_len = 0
    for i in range(len(arr)):
        cnt = 0
        for j in range(len(arr[i])):
            cnt += 1
            if max_len < cnt :
                max_len = cnt

    for i in range(len(arr)):
        if len(arr[i]) != max_len:
            while len(arr[i]) < max_len:
                arr[i].append('히히')
    result = ''
    for i in range(max_len):
        for j in range(max_len):
            try:
                if arr[j][i] != '히히':
                    result += arr[j][i]
            except:
                pass

    print(f'#{tc} {result}')
