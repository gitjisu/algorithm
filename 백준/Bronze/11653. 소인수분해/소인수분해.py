import sys

n = int(input())

# 2로 나누기
while n % 2 == 0:
    print(2)
    n //= 2

# 3으로 나누기
while n % 3 == 0:
    print(3)
    n //= 3

# 5부터 sqrt(n)까지의 홀수로 나누기
factor = 5
while factor * factor <= n:
    while n % factor == 0:
        print(factor)
        n //= factor
    while n % (factor + 2) == 0:
        print(factor + 2)
        n //= (factor + 2)
    factor += 6

# 만약 n이 1이 아닌 소수라면 출력
if n > 1:
    print(n)
