import sys
sys.stdin = open('1.txt')


def dfs(arr, v, dfs_lst):
    global cnt
    dfs_lst[v] = 1
    cnt += 1
    for i in range(len(arr[v])):
        if dfs_lst[i] != 1 and arr[v][i] == 1:
            dfs(arr, i, dfs_lst)
    return cnt

n = int(input())
m = int(input())
arr = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    p, c = map(int, input().split())
    arr[p][c] = 1
    arr[c][p] = 1


dfs_lst = [0] * (n+1)
v = 1
cnt = 0
dfs(arr, v, dfs_lst)
print(cnt-1)