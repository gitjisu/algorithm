import sys
sys.stdin = open('헌터.txt')
from itertools import permutations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global min_hour, test_hour, point, arr
    if test_hour < min_hour:
        test_hour = min_hour
        return 
    for i in range(point):
        for j in range(point):
            if arr[i][j] != 0 and arr[i][j] != 'hunter':
                cnt = 0
                for k in range(4):
                    for v in range(4):
                        ni = i + dx[k]
                        nj = j + dy[v]


t = int(input()) #테스트케이스

for tc in range(1, t+1):
    point = int(input())
    arr = [list(map(int, input().split()))for _ in range(point)]

    min_hour = 99999999 #최단시간 초깃값
    test_hour = 99999999 #테스트시간 초깃값
    people = []
    monster = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] > 0 :
                # 고객 위치
                people.append([arr[i][j], i, j])
            elif arr[i][j] < 0 :
                # 몬스터 위치
                monster.append([arr[i][j], i, j])

    road = people + monster
    print(road)


