import sys
sys.stdin = open('교수님.txt')
from pprint import pprint

def dfs(v):
    global visited
    stack = [v]                 # dfs의 출발 정점이 담긴 상태로 스택 초기화
    while stack:                # 스택이 비어있을때까지 반복
        v = stack.pop()         # 시작 정점을 스택에서 꺼냄
        if not visited[v]:      # 아직 방문하지 않은 정점이라면
            visited[v] = 1      # 방문 체크
            print(f'방문 정점: {v}, 방문 체크: {visited}')
            for j in range(1, V+1):                     # 시작 정점과 연결된 정점 찾기
                if G[v][j] == 1 and not visited[j]:     # v 정점과 연결된 정점이면서 아직 방문하지 않은 경우에만
                    stack.append(j)                     # 스택에 정점 추가

V, E = map(int, input().split())                        # V = 정점의 갯수 E = 간선의 갯수
temp = list(map(int, input().split()))                  # 연결된 정점 정보 입력
G = [[0]*(V+1) for _ in range(V+1)]                     # 2차원 행렬 초기화
visited = [0]*(V+1)                                     # 방문 정점 표시할 리스트 초기화
for i in range(E):                                      # 방향성이 없으므로
    G[temp[i * 2]][temp[i * 2 + 1]] = 1                 # 시작 정점 행에 연결된 정점 열을 1로 변경
    G[temp[i * 2 + 1]][temp[i * 2]] = 1                 # 시작 정점 열에 연결된 정점 행도 1로 변경
# pprint(G)

dfs(2)