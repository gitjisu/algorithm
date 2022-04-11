import sys
import pprint
sys.stdin = open('1.txt')

arr = [[0] * 100 for _ in range(100)]
cnt = 0
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2): # 1 2 3
        for k in range(y1, y2): # 2 3
            if arr[k][j] == 0:
                arr[k][j] = 1
                cnt += 1
print(cnt)