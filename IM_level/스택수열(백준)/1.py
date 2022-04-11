import sys
sys.stdin = open('1.txt')

n = int(input()) # 8
stack = []
total = []
num = 1
for i in range(n):
    arr = int(input())

    while num <= arr:
        total.append("+")
        stack.append(num)
        num += 1
    if stack[-1] == arr:
        total.append("-")
        stack.pop() # 리스트의 마지막 요소 꺼내기
    else:
        print("NO")
        break
print("\n".join(total))
