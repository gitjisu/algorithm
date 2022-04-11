import sys
sys.stdin = open('1.txt')

def find(x):
    if x == parent[x]:
        return x
    else:
        return find(parent[x])


def union(a, b):
    parent[find(a)] = find(b)

t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    mlst = list(map(int, input().split()))

    for i in range(m):
        union(mlst[i*2+1], mlst[i*2])

    result = []
    for i in range(1, n+1):
        result.append(find(i))

    print(len(set(result)))

