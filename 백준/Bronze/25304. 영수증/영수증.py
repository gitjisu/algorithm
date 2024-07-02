

# 총 금액
total = int(input())
# 검산
result = 0

# 종류 수 
tc = int(input())
# 가격, 갯수

for i in range(0, tc) :
  a, b = map(int, input().split())
  result += a * b

if result == total :
  print('Yes')
else :
  print('No')