import sys
from turtle import st
sys.stdin = open('5.txt')

t = int(input())

for tc in range(t):
      arr = list(map(int, input().split()))
      
      total = 0
      student = 0
      for i in range(len(arr)):
            if i == 0:
                  student = arr[i]
            if i != 0:
                  total += arr[i]
      
      avg = total//student
      
      high_student = 0
      for i in range(len(arr)):
            if i != 0 and arr[i]> avg:
                  high_student += 1  
     
      a = high_student / student * 100
      result = round(a, 3)
      print(f'{result:.3f}%')


      
