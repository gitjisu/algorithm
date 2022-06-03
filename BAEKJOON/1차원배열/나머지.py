import sys

from pyparsing import restOfLine
sys.stdin = open('4.txt')

# 총 테스트케이스 3
t = 3
for tc in range(t):
      arr = [] 
      for i in range(10):
            arr.append(int(input()))
      
      result = []
      for i in arr:
            result.append(i%42)
      
      a = set(result)
      print(len(a))
      