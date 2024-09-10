import sys

t = int(input())
result = 0
for _ in range(t) :
  prev =[]
  word = input()
  for w in word :
    if w in prev :
      lastWord = prev[-1]
      if lastWord == w:
        prev.append(w)
      else :
        break
    else :
      prev.append(w)
  
  if ('').join(prev) == word :
    result += 1


print(result)
