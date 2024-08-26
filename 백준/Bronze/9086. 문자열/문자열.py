import sys


t = int(input())

for tc in range(t):
  word = input()
  print(word[0],word[len(word)-1], sep='')