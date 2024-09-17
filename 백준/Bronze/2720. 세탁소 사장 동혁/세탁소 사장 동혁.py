import sys

unit = {
  'Q' : 25,
  'D' : 10,
  'N' : 5,
  'P' : 1
}

t = int(input())

for _ in range(t) :
  change = int(input())
  temp = [0 for _ in range(4)]
  order = 0
  for u in unit :
    temp[order] = change//unit[u]
    order += 1
    change = change%unit[u]

  print(' '.join(map(str, temp)))   




  
