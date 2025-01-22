import sys


def dfs(computer_index) :

  # computer_index = 1
  visited[computer_index] = True
  # [0False, 1True, 2True, 3False, 4False, 5True, 6True]

  for i in graph[computer_index] :
    if visited[i] == False :
      global answer
      answer += 1
      dfs(i)



# 7
computer_num = int(input()) 
# 6
computer_pair = int(input())



# 컴퓨터 칸을 만들고 1부터 시작하니까 +1
graph = [[] for _ in range(computer_num + 1)]
# visited 배열을 만든다
visited = [False] * (computer_num + 1)

answer = 0
for _ in range(computer_pair) :
  a, b = map(int, input().split())
  # 양방향 그래프
  graph[a].append(b)
  graph[b].append(a)


dfs(1)
print(answer)