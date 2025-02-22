import sys

time = int(input())

button = [300, 60, 10]

result = [0, 0, 0]

for i in range(3) :
    if time >= button[i]:
        result[i] = time // button[i]
        time %= button[i]
    
if (time != 0) :
    print(-1)
else :
  print(result[0], result[1], result[2])