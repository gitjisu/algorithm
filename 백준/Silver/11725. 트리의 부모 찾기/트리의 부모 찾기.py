import sys
sys.setrecursionlimit(10**6)
n = int(input())


def dfs(v) :
  for i in graph[v] :
    
    if answer[i] == 0 :
      
      answer[i] = v
      dfs(i)


graph = [[] for _ in range(n+1)]
answer =[0] * (n + 1) 

for _ in range(n-1) :
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)




dfs(1)

for i in range(2, n+1) :
  print(answer[i])