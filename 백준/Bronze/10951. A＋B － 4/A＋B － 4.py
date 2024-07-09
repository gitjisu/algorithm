import sys


tc = sys.stdin.read().splitlines()

for i in range(0, len(tc)) :
  a,b= map(int, tc[i].split())
  print(a+b)