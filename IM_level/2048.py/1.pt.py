import sys
sys.stdin = open('1.txt')
n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
print(arr)
lst = []
for i in range(n):
    for j in range(n):
        cnt = 0
        while cnt < 6:
            if arr[i][j] == arr[i+1][j] or arr[i][j] == arr[i][]