import sys
sys.stdin = open('5356.txt')

t = int(input())
for tc in range(1, t+1):
    arr = []
    for i in range(5):
        arr.append(list(map(str, input().split())))
    print(arr)