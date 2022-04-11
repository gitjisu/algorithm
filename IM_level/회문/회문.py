import sys
sys.stdin = open('회문.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(str, input()))for _ in range(n)]
    #가로방향
    for i in range(n): #0
        for j in range(n-m+1): #0
            temp = [] G
            for k in range(m): #10
                temp.append(arr[i][j+k]) #0 #0
            if temp == temp[::-1]:
                result = ''.join(temp)

    #열
    for i in range(n):
        for j in range(n-m+1):
            temp = []
            for k in range(m):
                temp.append(arr[j+k][i])
            if temp == temp[::-1]:
                result = (''.join(temp))

    print(f'#{tc} {result}')

