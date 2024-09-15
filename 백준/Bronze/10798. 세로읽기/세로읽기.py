import sys

input = sys.stdin.read
data = input().strip().split('\n')


arr = [line for line in data]

maxLen = max(len(line) for line in arr)


result = ''
for i in range(len(arr)) :
  
  if (len(arr[i]) < maxLen) :
    cnt = maxLen - len(arr[i])
    arr[i] += '*' * cnt


for i in range(maxLen) :
  for j in range(5) :
    
    if arr[j][i] != '*' :
      result += arr[j][i]

print(result)
    