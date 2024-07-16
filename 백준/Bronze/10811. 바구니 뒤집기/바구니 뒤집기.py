

# 바구니 n개
# m번 바구니의 순서를 역순으로 만든다
n,m = map(int, input().split())

result = [i for i in range(1, n+1)]

for x in range(m) :
  i, j = map(int, input().split())
  
  temp = result[i-1:j]
  temp.reverse()
  result[i-1:j] = temp

print(" ".join(map(str, result)))




  