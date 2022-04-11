TC = int(input())                                        TC = int(input())
for tc in range(1, TC+1):
    X, Y = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(X)]
    maxV = 0
    for i in range(X):
        cnt = 0
        for j in range(Y):
            if lst[i][j] == 1:
                cnt += 1
                if cnt > maxV:
                    maxV = cnt
            else:
                cnt = 0
    for i in range(Y):
        cnt = 0
        for j in range(X):
            if lst[j][i] == 1:
                cnt += 1
                if cnt > maxV:
                    maxV = cnt
            else:
                cnt =0
    print('#{} {}'.format(tc, maxV))