import sys
sys.stdin = open('1.txt')

for tc in range(1, 11):
    num = int(input())
    arr = [list(map(str, input())) for _ in range(100)]

    for i in range(100):
        for j in range(

