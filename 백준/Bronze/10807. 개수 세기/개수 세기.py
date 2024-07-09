import sys


t = sys.stdin.read().splitlines()

result = 0
n = int(t[0])
arr = t[1].split()
v = t[2]

for i in arr:
  if i == v :
    result += 1


print(result)