import sys


a, b = map(str, input().split())

print(int(a[::-1]) if  int(a[::-1]) > int(b[::-1]) else int(b[::-1]))

