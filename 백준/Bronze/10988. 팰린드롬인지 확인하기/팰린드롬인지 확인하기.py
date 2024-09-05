
import sys
input = sys.stdin.read

word = input().strip()

print(1 if word == word[::-1] else 0)