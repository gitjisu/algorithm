import sys

input = sys.stdin.read()
lines = input.splitlines()

for line in lines:
    a, b = map(int, line.split())
    if a == 0 and b == 0:
        break
    print(a + b)
