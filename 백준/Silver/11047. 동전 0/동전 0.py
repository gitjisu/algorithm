import sys


n, k = map(int, input().split())

coins = sorted([int(input()) for _ in range(n)], reverse=True)
result = 0



while k > 0 :
  currentCoin = coins.pop(0)

  
  result += k // currentCoin
  k = k % currentCoin




print(result)