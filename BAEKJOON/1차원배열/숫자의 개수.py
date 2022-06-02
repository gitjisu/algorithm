import sys
sys.stdin = open('3.txt')

a = int(input())

b = int(input())

c = int(input())

result = a*b*c

result2 = str(result)

result3 = []

for i in result2:
      result3.append(int(i))


ans = [0]*10
for i in result3:
      ans[i] += 1

for i in ans:
      print(i)


      

