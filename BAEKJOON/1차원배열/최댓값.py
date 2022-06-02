import sys
sys.stdin = open('2.txt')


arr = []
for i in range(9):
      arr.append(int(input()))
      
a = max(arr)
print(a)
print(arr.index(a)+1)