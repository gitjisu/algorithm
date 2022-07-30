import sys
sys.stdin = open('9.txt')

a, b, c = map(int, input().split())

print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

