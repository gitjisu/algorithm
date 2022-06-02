import sys
sys.stdin = open('1.txt')

n = int(input())
lst = list(map(int, input().split()))
print(min(lst),max(lst))                       