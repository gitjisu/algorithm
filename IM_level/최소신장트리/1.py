import sys
sys.stdin = open('1.txt')

def find(x, y):
    return get(x) == get(y)

def get(x):
    if parent[x] != x:
        parent[x] = get(parent
                        [x])
        return parent[x]

def union(x, y):
    a = get(x)
    b = get(y)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a


t = int(input())
for tc in range(1,t+1):
    v, e = map(int, input().split())
    parent = [i for i in range(v+1)]
    edge = [list(map(int, input().split()))for _ in range(e)]
    edge.sort(key=lambda x: -x[2])

    result = 0
    while edge:
        a, b, v = edge.pop()
        if not find(a, b):
            union(a, b)
            result += v

    print(result)