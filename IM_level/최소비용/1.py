import sys
sys.stdin = open('1.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def find(i, j):
    dist[i][j] = 0 # 시작 값 0
    q = deque()
    q.append((i, j)) # 시작점 큐에 넣기
    while q:
        y, x = q.popleft()
        for k in range(4): # 델타검색
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                temp = 1 # 기본비용
                if arr[nx][ny] > arr[x][y]: #높이 차이가 나면
                    temp += arr[nx][ny] - arr[x][y] # 그높이가 가중치
                if dist[nx][ny] > dist[x][y] + temp: # 새롭게 갈 좌표의 최단거리가 현위치의 최단거리 + 가중치
                    dist[nx][ny] = dist[x][y] + temp
                    q.append((nx, ny))

    return dist[n-1][n-1]


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]
    inf = 9999999999
    dist = [[inf] * n for _ in range(n)] #최단거리배열
    print(find(0, 0))


    