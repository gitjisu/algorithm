import sys


t = int(input())

result = []
for tc in range(t) :
  r, word = input().split(' ')
  temp = ''
  for w in word:
    temp += w*int(r)
  result.append(temp)
print(('\n').join(result))